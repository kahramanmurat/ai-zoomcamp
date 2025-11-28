# Django Todo Application

A beautiful and modern TODO application built with Django that allows you to create, edit, delete, and manage todos with due dates.

## Features

- ✅ Create, edit, and delete TODOs
- 📅 Assign due dates to todos
- ✓ Mark TODOs as resolved/unresolved
- 🔍 Filter todos by status (All, Pending, Resolved, Overdue)
- ⚠️ Overdue todos are automatically highlighted
- 🎨 Modern, responsive UI with Bootstrap 5

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation & Setup

### Step 1: Install Dependencies

Install Django and other required packages:

```bash
pip install -r requirements.txt
```

Or if you prefer using a virtual environment (recommended):

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Run Database Migrations

Create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: (Optional) Create Admin User

Create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin account.

### Step 4: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Step 5: (Optional) Create Example Tasks

Populate the database with example tasks to see the application in action:

```bash
python manage.py create_example_tasks
```

This will create 12 example tasks including:
- Some resolved tasks
- Some pending tasks  
- Some overdue tasks
- Tasks with various due dates

To clear all existing tasks and create fresh examples:

```bash
python manage.py create_example_tasks --clear
```

### Step 6: Access the Application

Open your web browser and navigate to:

- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Usage

### Creating a Todo

1. Click the "Create New Todo" button on the homepage
2. Fill in the title (required)
3. Optionally add a description
4. Set a due date and time (optional)
5. Click "Save Todo"

### Editing a Todo

1. Click the "Edit" button on any todo card
2. Modify the fields as needed
3. Click "Save Todo"

### Marking as Resolved

1. Click the "Resolve" button on any pending todo
2. The todo will be marked as resolved and grayed out
3. Click "Unresolve" to mark it as pending again

### Deleting a Todo

1. Click the "Delete" button on any todo card
2. Confirm the deletion

### Filtering Todos

Use the filter buttons at the top to view:
- **All**: Show all todos
- **Pending**: Show only unresolved todos
- **Resolved**: Show only completed todos
- **Overdue**: Show todos past their due date

## Project Structure

```
week-01/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── todo_project/            # Main project directory
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL configuration
│   └── ...
├── todos/                   # Todos application
│   ├── models.py            # Todo model definition
│   ├── views.py             # View functions
│   ├── forms.py             # Form definitions
│   ├── urls.py              # App URL configuration
│   └── templates/           # HTML templates
│       └── todos/
│           ├── base.html
│           ├── todo_list.html
│           ├── todo_form.html
│           └── todo_confirm_delete.html
└── db.sqlite3               # SQLite database (created after migrations)
```

## Troubleshooting

### Django not found

If you get an error that Django is not installed:
```bash
pip install Django
```

Or install all requirements:
```bash
pip install -r requirements.txt
```

### Port already in use

If port 8000 is already in use, you can specify a different port:
```bash
python manage.py runserver 8001
```

### Database errors

If you encounter database-related errors, try:
```bash
python manage.py migrate --run-syncdb
```

## Development

The application uses SQLite by default for development. The database file (`db.sqlite3`) will be created automatically when you run migrations.

For production deployment, you should:
- Change `DEBUG = False` in `settings.py`
- Set a secure `SECRET_KEY`
- Configure a production database (PostgreSQL, MySQL, etc.)
- Set up proper static file serving
- Configure `ALLOWED_HOSTS`

## License

This project is part of the AI Zoomcamp course.

