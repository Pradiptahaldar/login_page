# 🔐 Flask Login System

A simple and secure login & registration system built using **Flask, MySQL, HTML, and CSS**.

This project demonstrates how to create a full-stack authentication system with backend integration and session handling.

---

## 🚀 Features

* User Registration
* User Login Authentication
* Session Management
* MySQL Database Integration
* Clean and Minimal UI

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Database:** MySQL

---

## 📁 Project Structure

```
login-system-flask/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   └── dashboard.html
│
├── static/
│   └── style.css
│
├── database/
│   └── schema.sql
│
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/yourusername/login-system-flask.git
cd login-system-flask
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Setup MySQL Database

* Open MySQL
* Run the SQL file:

```
source database/schema.sql;
```

---

### 4. Configure Database

Update your MySQL credentials inside `app.py`:

```
host="localhost",
user="root",
password="yourpassword",
database="login_db"
```

---

### 5. Run the Application

```
python app.py
```

---

### 6. Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🔐 Future Improvements

* Password Hashing (Security Enhancement)
* User Logout Feature
* Form Validation
* Responsive UI Design
* Deployment (Render / Railway / Vercel backend)

---

## ⚠️ Note

Currently, passwords are stored in plain text.
For production use, always hash passwords using:

```
werkzeug.security
```

---

## 👨‍💻 Author

Pradipta Haldar

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub and feel free to improve it!
