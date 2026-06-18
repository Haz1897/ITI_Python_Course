from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, "list.html", {"books": books})

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.views += 1
    book.save()
    return render(request, "details.html", {"book": book})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "form.html", {"action": "Add", "form": form})

def book_edit(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_detail", book_id=book_id)
    else:
        form = BookForm(instance=book)
    return render(request, "form.html", {"action": "Edit", "form": form})

def book_delete(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        Book.objects.get(pk=book_id).delete()
        return redirect("book_list")
    return render(request, "confirm_delete.html", {"book": book})