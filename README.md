# Rumi Press — Book Distribution Expense Tracker

> **📚 Coursera Project**
> This project was built as part of the [Build an Expense Tracker App in Django](https://www.coursera.org/learn/showcase-build-expense-tracker-app-django/) guided project on Coursera.

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
git clone https://github.com/ajitagupta/django-expense-tracker.git
cd django-expense-tracker

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install django openpyxl

# 4. Run migrations
python manage.py migrate

# 5. Import sample data
python manage.py import_books sample_books.xlsx

# 6. Create admin user
python manage.py createsuperuser

# 7. Run the server
python manage.py runserver
```

Then visit:
- http://127.0.0.1:8000/ — Books list
- http://127.0.0.1:8000/categories/ — Categories CRUD
- http://127.0.0.1:8000/report/ — Expense report with charts
- http://127.0.0.1:8000/admin/ — Django admin

## Sample Data

A sample spreadsheet (`sample_books.xlsx`) is included in the repository with 27 books across 10 categories (Business Analytics, Python, Data Science, Maths, Statistics, Deep Learning, NLP, SQL, Visualization, R Studio, Data Ethics). Use it to test the import command and explore the app right away.

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
└── sample_books.xlsx   # Sample dataset for testing
```
