# INTELLIBOT AI - PyCharm Project

## Technology
- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript

## Features
- IntelliBot chat assistant
- Business Office service guidance
- Registrar's Office service guidance
- Queue number generation
- Queue status API
- Service requests
- SQLite database
- Responsive dashboard

## Run in PyCharm

1. Open this folder as a project.
2. Make sure a Python 3 interpreter is selected.
3. Open the PyCharm Terminal.
4. Run:

   pip install -r requirements.txt

5. Run `app.py`.
6. Open:

   http://127.0.0.1:5000/

The SQLite database `intellibot.db` will be created automatically.

## Important
This is a capstone prototype. The chatbot is rule-based, so it does not yet use a generative AI model.

For a production system, add secure authentication, role-based access, server-side validation, audit logs, HTTPS, database backups, and an approved AI service/model. Do not put secret API keys in HTML or JavaScript.

Official transactions such as payments and release of academic records should remain controlled by authorized staff.
