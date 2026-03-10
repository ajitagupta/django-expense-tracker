from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="home"),

    # Categories
    path("categories/", views.category_list, name="category_list"),
    path("categories/new/", views.category_create, name="category_create"),
    path("categories/<int:pk>/edit/", views.category_edit, name="category_edit"),
    path("categories/<int:pk>/delete/", views.category_delete, name="category_delete"),

    # Books
    path("books/", views.book_list, name="book_list"),
    path("books/new/", views.book_create, name="book_create"),
    path("books/<int:pk>/edit/", views.book_edit, name="book_edit"),
    path("books/<int:pk>/delete/", views.book_delete, name="book_delete"),

    # Report
    path("report/", views.report, name="report"),
]
