"""
Management command: python manage.py import_books <path_to_xlsx>

Imports books and categories from the Rumi Press spreadsheet.
"""
import openpyxl
from django.core.management.base import BaseCommand
from tracker.models import Category, Book


class Command(BaseCommand):
    help = "Import books from the Rumi Press Excel spreadsheet"

    def add_arguments(self, parser):
        parser.add_argument("xlsx_path", type=str, help="Path to the .xlsx file")

    def handle(self, *args, **options):
        path = options["xlsx_path"]
        self.stdout.write(f"Opening {path} ...")

        wb = openpyxl.load_workbook(path)
        ws = wb.active

        created_books = 0
        skipped = 0
        category_cache = {}

        for i, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
            isbn, title, subtitle, authors, publisher, published_date, cat_name, expense = row[:8]

            if not title:
                continue

            # Normalise category name
            cat_name = (cat_name or "Uncategorised").strip().title()
            if cat_name not in category_cache:
                cat_obj, _ = Category.objects.get_or_create(name=cat_name)
                category_cache[cat_name] = cat_obj
            category = category_cache[cat_name]

            # Clean ISBN
            isbn_str = str(isbn).strip() if isbn else None

            # Handle published_date (already datetime from openpyxl)
            pub_date = published_date.date() if hasattr(published_date, "date") else None

            try:
                _, created = Book.objects.update_or_create(
                    isbn=isbn_str,
                    defaults={
                        "title": title,
                        "subtitle": subtitle,
                        "authors": authors,
                        "publisher": publisher,
                        "published_date": pub_date,
                        "category": category,
                        "distribution_expense": expense,
                    },
                )
                if created:
                    created_books += 1
                else:
                    skipped += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"  Row {i} skipped: {e}"))

        self.stdout.write(self.style.SUCCESS(
            f"Done! {created_books} books imported, {skipped} updated. "
            f"{len(category_cache)} categories."
        ))
