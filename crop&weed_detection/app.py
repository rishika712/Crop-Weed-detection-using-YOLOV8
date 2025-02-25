import streamlit as st
import sqlite3
from ultralytics import YOLO
from PIL import Image
import os
import asyncio

# Ensure asyncio event loop compatibility
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Database setup
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )''')
conn.commit()

# Model setup
MODEL_PATH = r'C:/Users/RISHIKA/Downloads/best.pt'
model = YOLO(MODEL_PATH)

# User authentication
def register_user(username, password):
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        st.success('Registration successful!')
    except sqlite3.IntegrityError:
        st.error('Username already exists!')

def login_user(username, password):
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    return c.fetchone()

# Function to set the background image
def set_background(image_file):
    page_bg_img = f'''
    <style>
        body {{
            background-image: url("data:image/jpg;base64,{image_file}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #FAFAFA;
            font-family: 'Sans serif';
        }}
        .stApp {{
            background-color: rgba(0, 0, 0, 0);
        }}
        [data-testid="stSidebar"] {{
            background-color: rgba(20, 148, 83, 0.8);
        }}
        .css-17eq0hr a {{
            color: white !important;
            font-weight: bold;
        }}
        .app-heading {{
            text-align: center;
            font-size: 3em;
            color: black;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 40px;
        }}
        .stAlert {{
            font-size: 1.2em;
            color: #FAFAFA;
        }}
        .stButton>button {{
            background-color: #14A553;
            color: white;
            font-size: 1.1em;
            border-radius: 8px;
            padding: 10px 20px;
        }}
        .stButton>button:hover {{
            background-color: #0F7E3E;
        }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Base64 image processing
def get_base64_image(image_path):
    import base64
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Application structure
def main():
    st.set_page_config(page_title="Crop & Weed Detection", page_icon="🌱", layout="wide")

    bg_image = get_base64_image('assets/pic.jpg')
    set_background(bg_image)

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    menu = ['Login', 'Register'] if not st.session_state.logged_in else ['Home', 'Logout']
    choice = st.sidebar.selectbox('Menu', menu)

    st.markdown("<div class='app-heading'>Crop & Weed Detection</div>", unsafe_allow_html=True)

    if choice == 'Login':
        st.subheader('Login Page')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')

        if st.button('Login'):
            if not username or not password:
                st.error("Username and Password cannot be blank!")
            elif not (any(char.isdigit() for char in password) and any(char.isalpha() for char in password)):
                st.error("Password must contain both letters and numbers!")
            elif len(password) > 12:
                st.error("Password must not exceed 12 characters!")
            else:
                user = login_user(username, password)
                if user:
                    st.success(f'Welcome {username}!')
                    st.session_state.logged_in = True
                    st.query_params.clear()
                else:
                    st.error('Invalid username or password')

    elif choice == 'Register':
        st.subheader('Create a New Account')
        new_user = st.text_input('Username')
        new_password = st.text_input('Password', type='password')

        if st.button('Register'):
            if not new_user or not new_password:
                st.error("Username and Password cannot be blank!")
            elif not (any(char.isdigit() for char in new_password) and any(char.isalpha() for char in new_password)):
                st.error("Password must contain both letters and numbers!")
            elif len(new_password) > 12:
                st.error("Password must not exceed 12 characters!")
            else:
                register_user(new_user, new_password)

    elif choice == 'Home' and st.session_state.logged_in:
        st.header('Upload an Image for Crop and Weed Detection')
        uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_container_width=True)
            with st.spinner('Processing...'):
                image_path = 'temp_image.png'
                image.save(image_path)
                results = model.predict(source=image_path, save=True, save_txt=True, project='runs', name='predict', exist_ok=True)
                if len(results[0].boxes) == 0:
                    st.warning('Neither crop nor weed detected in the image.')
                else:
                    st.success('Detection completed!')
                    result_dir = 'runs/predict'
                    for file in os.listdir(result_dir):
                        if file.endswith(('.png', '.jpg', '.jpeg')):
                            result_img_path = os.path.join(result_dir, file)
                            result_img = Image.open(result_img_path)
                            st.image(result_img, caption='Processed Image', use_container_width=True)
                            break
                    else:
                        st.error('Processed image not found.')

    elif choice == 'Logout':
        st.session_state.logged_in = False
        st.success('Logged out successfully!')
        st.query_params.clear()

if __name__ == '__main__':
    main()
