from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Count
from django.contrib import messages
from .models import Book, Category
from .forms import BookForm, CategoryForm
import json


def category_list(request):
    categories = Category.objects.annotate(
        book_count=Count("books"),
        total_expense=Sum("books__distribution_expense"),
    )
    return render(request, "tracker/category_list.html", {"categories": categories})


def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Category created.")
        return redirect("category_list")
    return render(request, "tracker/category_form.html", {"form": form, "action": "Create"})


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        messages.success(request, "Category updated.")
        return redirect("category_list")
    return render(request, "tracker/category_form.html", {"form": form, "action": "Edit"})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Category deleted.")
        return redirect("category_list")
    return render(request, "tracker/confirm_delete.html", {"object": category, "type": "category"})


def book_list(request):
    books = Book.objects.select_related("category")
    category_id = request.GET.get("category")
    if category_id:
        books = books.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, "tracker/book_list.html", {
        "books": books,
        "categories": categories,
        "selected_category": int(category_id) if category_id else None,
    })


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Book added.")
        return redirect("book_list")
    return render(request, "tracker/book_form.html", {"form": form, "action": "Add"})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, "Book updated.")
        return redirect("book_list")
    return render(request, "tracker/book_form.html", {"form": form, "action": "Edit"})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted.")
        return redirect("book_list")
    return render(request, "tracker/confirm_delete.html", {"object": book, "type": "book"})


def report(request):
    data = (
        Category.objects.annotate(
            total_expense=Sum("books__distribution_expense"),
            book_count=Count("books"),
        )
        .order_by("-total_expense")
    )
    labels = [c.name for c in data]
    expenses = [float(c.total_expense or 0) for c in data]
    counts = [c.book_count for c in data]
    return render(request, "tracker/report.html", {
        "categories": data,
        "labels_json": json.dumps(labels),
        "expenses_json": json.dumps(expenses),
        "counts_json": json.dumps(counts),
        "total_expense": sum(expenses),
        "total_books": sum(counts),
    })
