# Upskill Campus Repository

## Crop & Weed Detection Using YOLOv8 🌱

### 📁 Project Overview
This repository contains a Streamlit-based web application that uses YOLOv8 for crop and weed detection from images. It includes user authentication and allows users to upload images for plant analysis. The project was developed during the internship at Upskill Campus, focusing on AI/ML techniques, data analytics, and related technologies.

---

## 🚀 Features
- ✅ **User Authentication** (Login/Register)
- ✅ **Crop & Weed Detection** using **YOLOv8**
- ✅ **Streamlit Web Interface** for easy interaction
- ✅ **Database (SQLite)** for storing user credentials

---

## 📦 Installation

1. **Clone the Repository:**
```bash
git clone https://github.com/rishika712/upskillCampus.git
cd Crop-Weed-Detection
```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Download YOLOv8 Model Weights:** (Replace with the correct path)
```bash
mv best.pt path/to/model/best.pt
```

4. **Run the Application:**
```bash
streamlit run Crop&WeedDectionUsingYOLOv8.py
```

---

## 📚 How It Works
1. **User Registration/Login**
2. **Upload an Image** (Crop/Weed Image)
3. **YOLOv8 Model Processes the Image**
4. **Detection Results Displayed**

---

## 📂 Folder Structure

📦 Crop-Weed-Detection  
 ├── 📜 Crop&WeedDectionUsingYOLOv8.py  # Main Streamlit app  
 ├── 📜 best.pt                         # YOLOv8 Model weights  
 ├── 📜 users.db                        # SQLite database  
 ├── 📂 runs                             # YOLOv8 results folder  
 ├── 📂 assets                           # Background images & UI assets  
 ├── 📜 requirements.txt                 # Dependencies  
 ├── 📜 README.md                        # Project Documentation  

---

## 🛠️ Technologies Used
- Python
- Machine Learning & Deep Learning
- YOLOv8 (Ultralytics) for object detection
- Streamlit for web interface
- SQLite3 for database management
- PIL (Pillow) for image processing
- OS & Asyncio

---

## 🚀 Future Improvements
- 🔹 Improve **UI/UX** with better visualization
- 🔹 Enhance **model accuracy** by training on a larger dataset
- 🔹 Implement **role-based access control**

---

## 👥 Author
Developed by **RISHIKA S** and **TRIPARNA ROY**

---

## 📄 License
This project is licensed under the **MIT License**.

---

