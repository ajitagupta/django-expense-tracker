from django.contrib import admin
from .models import Category, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "book_count")
    search_fields = ("name",)

    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = "# Books"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "authors", "publisher", "published_date", "category", "distribution_expense")
    list_filter = ("category",)
    search_fields = ("title", "authors", "publisher", "isbn")
    list_editable = ("distribution_expense",)
    date_hierarchy = "published_date"
    ordering = ("title",)
    fieldsets = (
        ("Book Info", {
            "fields": ("isbn", "title", "subtitle", "authors", "publisher", "published_date")
        }),
        ("Distribution", {
            "fields": ("category", "distribution_expense")
        }),
    )
