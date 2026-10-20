# Smart Campus Wallet

A digital wallet web app for managing purchases across a university campus. Built with Flask, SQLAlchemy and Bootstrap.

> **Status: early development.** User registration and login are working. The wallet features (balance, top-ups, payments) are planned but not built yet. See the [Roadmap](#roadmap).

## Features

- **User registration** with name, email and password
- **Secure password storage** using Werkzeug password hashing (no plain-text passwords)
- **Login** with clear error messages for unknown emails and wrong passwords
- **Session management** with a 30-minute session lifetime
- **Duplicate email protection** enforced both in the app and by a unique database constraint
- **Flash messages** for success and error feedback
- **Responsive UI** using Bootstrap 5 and Jinja2 templates

## Tech Stack

| Layer | Technology |
| --- | --- |
| Backend | Python, Flask |
| Database | SQLite via Flask-SQLAlchemy |
| Auth | Werkzeug password hashing, Flask sessions |
| Frontend | Jinja2 templates, Bootstrap 5.3 |

## Project Structure

```
Smart-Student-Campus-Wallet/
├── app.py                  # Entry point
├── app/
│   ├── __init__.py         # App factory, config, and routes (home, register, login)
│   ├── extensions.py       # SQLAlchemy instance
│   ├── models.py           # User model
│   ├── routes/             # Reserved for splitting routes into blueprints
│   ├── static/             # style.css, index.js
│   └── templates/          # base, index, login, register
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.9 or newer
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/TypicalW/Smart-Student-Campus-Wallet.git
   cd Smart-Student-Campus-Wallet
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv env

   # macOS / Linux
   source env/bin/activate

   # Windows
   env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install flask flask-sqlalchemy
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

5. Open **http://127.0.0.1:5000** in your browser.

The SQLite database (`campus_wallet.db`) is created automatically on first run inside the `instance/` folder.

## Usage

| Route | Methods | Description |
| --- | --- | --- |
| `/` | GET | Home page |
| `/register` | GET, POST | Create a new account |
| `/login` | GET, POST | Log in to an existing account |

## Database Schema

**`users`**

| Column | Type | Constraints |
| --- | --- | --- |
| `id` | Integer | Primary key |
| `name` | String(100) | Required |
| `email` | String(120) | Required, unique |
| `password` | String(255) | Required (hashed) |

## Roadmap

Planned features, in no fixed order:

- [ ] Logout and protected routes
- [ ] Wallet balance per user
- [ ] Top-up and transaction history
- [ ] Campus payments (cafeteria, library, stationery)
- [ ] User dashboard
- [ ] Admin and merchant roles
- [ ] Move configuration (secret key, database URL) to environment variables
- [ ] Add `requirements.txt` and automated tests

## Contributing

Contributions, issues and feature requests are welcome. Fork the repo, create a feature branch, and open a pull request.

## Author

**Ashmit Mishra**
