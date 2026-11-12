# CampusConnect

**Developer:** John Thomas Boltron  
**Section:** G5

## Description

CampusConnect is a Django web application that allows users to create accounts, log in, and manage their personal profiles. It includes role-based access for students and administrators.

## Features

- User registration and login
- Profile viewing and editing
- Django messages for signup success notifications
- Bootstrap 5 user interface
- Role-based admin panel access
- Protected pages requiring authentication

## Requirements

- Python
- Django

## Installation and Setup

1. Clone the repository.
2. Open the project folder in your terminal.
3. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

4. Activate the virtual environment:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```powershell
   python manage.py migrate
   ```

7. Start the development server:

   ```powershell
   python manage.py runserver
   ```

8. Open `http://127.0.0.1:8000/` in your browser.
