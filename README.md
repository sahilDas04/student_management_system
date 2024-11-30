# Student Management System

This repository contains a simple **Student Management System** built with **Django** for the backend and **HTML/CSS** for the frontend. The system allows managing students, courses, and their performance data, providing basic CRUD functionalities and an intuitive interface for easy use.

---

## 📋 **Features**
- **Student Management**: Add, view, update, and delete student information.
- **Course Management**: Manage available courses and their details.
- **Performance Tracking**: Record and view student grades and performance.
- **Authentication**: Basic login/logout functionality for administrators.
- **Responsive Design**: Frontend designed with HTML/CSS for a clean and responsive user experience.

---

## 🖼️ **Screenshots**

### **1. Dashboard View**
![Dashboard](images/dashboard.png)

### **2. Student Management Page**
![Student Management](images/student_management.png)

---

## 🛠️ **Technologies Used**
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default Django database, easy to set up and use)
  
---

## ⚙️ **Installation Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/student_management_system.git
cd student-management-system
```

### **2. Creating Virtual Envoirment**
```bash
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
```

### **3. Installing Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Create a Superuser**
```bash
python manage.py createsuperuser
```

### **6. Run the Server**
```bash
python manage.py runserver
```

### **7. Access the Application**
```bash
http://127.0.0.1:8000/  # Open your web browser and go to
```
