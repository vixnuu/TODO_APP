# 📝 TodoApp (Django)

A simple and user-friendly **Todo Management Web Application** built with **Django**.  
This project includes secure user authentication, full CRUD operations for todos, and a basic product image upload feature.

---

## 🚀 Features

### 🔐 Authentication System
- User Registration
- User Login
- User Logout
- Session-based Authentication using Django Authentication System

### ✅ Todo Management (CRUD)
Authenticated users can:
- Create new todos
- View todo details
- Update existing todos
- Delete todos
- View all their todos on the dashboard/home page

### 📁 File Upload Feature
- Upload product images
- Store product name and price
- Display uploaded products in a list view

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Programming Language |
| Django | Backend Framework |
| SQLite | Database |
| HTML/CSS | Frontend Templates |
| Django Templates | Dynamic Rendering |
| Django Authentication | User Authentication |

---

## 📂 Project Structure

```bash
TodoApp/
│
├── todoproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── db.sqlite3
│
├── todoapp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── media/
├── env/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/todoapp.git
cd todoapp
```

---

### 2️⃣ Create & Activate Virtual Environment

#### Windows (PowerShell)

```powershell
python -m venv env
env\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv env
source env/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Database Migrations

```bash
python manage.py migrate
```

---

### 5️⃣ Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```bash
http://127.0.0.1:8000/
```

---


## 🔒 Authentication

This project uses Django’s built-in authentication system for:
- Secure user login/logout
- Password hashing
- Session management
- Route protection for authenticated users

---

## 📌 Future Improvements

- Add task completion status
- Add due dates and reminders
- Search and filter todos
- Responsive UI improvements
- Deploy using Render/Heroku/AWS
- Add REST API using Django REST Framework

---

## 👨‍💻 Author

**Vishnu KV**  
Computer Science Graduate | Django Developer

---

## 📄 License

This project is created for learning and portfolio purposes.
