# Notes App

A simple Django notes application with a polished frontend for creating, viewing, editing, and deleting notes.

## Features

- Create new notes
- View notes in a card-based dashboard
- Edit and delete existing notes
- Responsive UI with custom CSS and JavaScript
- Flash messages, copy-to-clipboard, and delete confirmation on the detail page

## Tech Stack

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite

## Project Structure

- `manage.py` - Django management entry point
- `notes/` - Main app containing models, views, forms, templates, and static assets
- `notesapp/` - Project configuration
- `db.sqlite3` - Local SQLite database

## Setup

1. Create and activate a virtual environment.
2. Install dependencies.
3. Run migrations.
4. Start the development server.

```bash
python -m venv venv
source venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver
```

## Usage

- Open the home page to see all notes.
- Click **New note** to create a note.
- Open a note to edit, copy, or delete it.

## Notes

The app uses Django templates plus custom static files in `notes/static/notes/` for the frontend styling and interaction behavior.
