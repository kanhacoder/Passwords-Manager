# 🔐 Password Manager

A terminal-based Password Manager built using **Python** and **MySQL**. It allows users to create multiple profiles, securely manage account credentials, and perform CRUD operations on stored passwords through a simple command-line interface.

---

## 🚀 Features

- 👤 Create multiple user profiles
- 🔑 Login with a master password
- ➕ Add new account credentials
- 👀 View stored account passwords
- ✏️ Update usernames and passwords
- 🗑️ Delete stored accounts
- 📋 View all saved account platforms
- 🗄️ MySQL database integration

---

## 🛠️ Tech Stack

- Python 3
- MySQL
- mysql-connector-python

---

## 📂 Project Structure

```
PasswordManager/
│
├── main.py
├── database.py
├── requirements.txt
├── README.md
└── sql/
    └── schema.sql
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/PasswordManager.git
```

### 2. Install dependencies

```bash
pip install mysql-connector-python
```

### 3. Create the database

Run the SQL script located in:

```
sql/schema.sql
```

### 4. Configure MySQL

Open `database.py` and update:

```python
host = "localhost"
user = "your_username"
password = "your_password"
database = "passwordsDB"
```

### 5. Run the project

```bash
python main.py
```

---

## 📖 Database Schema

### profile_id

| Column | Type |
|--------|------|
| profile_id | INT |
| username | VARCHAR(50) |
| master_password | VARCHAR(255) |

### passwords

| Column | Type |
|--------|------|
| password_id | INT |
| profile_id | INT |
| website | VARCHAR(100) |
| username | VARCHAR(100) |
| password | VARCHAR(255) |

---

## 📌 Current Features

- Profile Creation
- Profile Login
- Add Account
- View Account
- View Password
- Update Username & Password
- Delete Account

---

## 🔮 Future Improvements

- Password encryption
- Password strength checker
- Random password generator
- Forgot password functionality
- Password expiry reminders
- Export and import encrypted backups
- Graphical User Interface (GUI)

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

---

## 📄 License

This project is licensed under the MIT License.