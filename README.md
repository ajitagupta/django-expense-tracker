# Rumi Press — Book Distribution Expense Tracker

A Django web app to manage book distribution expenses for Rumi Press.

## Features
- **CRUD for Categories** — add/edit/delete book categories (Business Analytics, Python, etc.)
- **CRUD for Books** — full book management with title, authors, publisher, date, category, and expense
- **Data Import** — management command to import from the Excel spreadsheet
- **Expense Report** — bar chart + doughnut chart + table showing expenses per category (Chart.js)
- **Django Admin** — full admin dashboard at `/admin/`

## Quickstart

```bash
# 1. Clone and set up
git clone <your-repo>
cd rumipress

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install django openpyxl

# 4. Run migrations
python manage.py migrate

# 5. Import data from spreadsheet
python manage.py import_books path/to/Books_Distribution_Expenses.xlsx

# 6. Create admin user
python manage.py createsuperuser

# 7. Run the server
python manage.py runserver
```

Then visit:
- http://127.0.0.1:8000/ — Books list
- http://127.0.0.1:8000/categories/ — Categories CRUD
- http://127.0.0.1:8000/report/ — Expense report with charts
- http://127.0.0.1:8000/admin/ — Django admin (login: admin / admin123)

## Data Models

**Category**
- `name` (unique)

**Book**
- `isbn`, `title`, `subtitle`, `authors`, `publisher`
- `published_date`, `category` (FK), `distribution_expense`

## Project Structure
```
rumipress/
├── rumipress/          # Project config (settings, urls)
├── tracker/            # Main app
│   ├── models.py       # Category, Book
│   ├── views.py        # CRUD + report views
│   ├── forms.py        # ModelForms
│   ├── admin.py        # Admin config
│   ├── urls.py         # URL routing
│   ├── templates/tracker/
│   │   ├── base.html
│   │   ├── book_list.html / book_form.html
│   │   ├── category_list.html / category_form.html
│   │   ├── confirm_delete.html
│   │   └── report.html
│   └── management/commands/
│       └── import_books.py
└── db.sqlite3          # SQLite database
```
