# 🎓 Student Record Management System

A simple web-based CRUD application built using **Flask**, **Python**, and **SQLite** for managing student records securely via an admin dashboard.

> 🔗 Live Demo: _Coming Soon_  
> 👨‍💻 Developed by [Kolipaka Akhil Surya](https://www.linkedin.com/in/akhilsurya/)

---

## 🔧 Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML, CSS (Jinja2 Templates)
- **Authentication:** Session-based Admin Login

---

## 🚀 Features

- 🔐 **Secure Admin Login** (hardcoded credentials for demo)
- 📋 **Dashboard View** of all student records
- ➕ **Add** new student
- ✏️ **Edit** student details
- ❌ **Delete** student record
- 🚪 **Logout** to end session

---

## 📁 Project Structure

Student-Record-Management-System/

│
├── templates/ # HTML templates (login.html, dashboard.html, add.html, edit.html)

├── static/ # Static files (CSS, images if any)

├── students.db # SQLite database (auto-generated)

├── app.py # Main Flask application

└── README.md # Project README


---

## 🔑 Admin Credentials (Demo)

> Username: `admin`  
> Password: `admin123`

---

## 🛠️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/AkhilSuryaK/Student-Record-Management-System.git
cd Student-Record-Management-System

Install dependencies
pip install Flask Flask-SQLAlchemy

Run the app
python app.py

Open in browser
http://127.0.0.1:5000/

📌 Important Notes
Admin credentials are hardcoded for simplicity. For production, use a proper authentication system.
Database is SQLite (students.db) and is created automatically on first run.

🤝 Connect with Me
GitHub: @AkhilSuryaK
LinkedIn: Akhil Surya Kolipaka

📃 License
This project is open-source and free to use under the MIT License.
Let me know if you also want help generating badges (e.g., Python version, license) or auto-deploy it with Render/Heroku.





