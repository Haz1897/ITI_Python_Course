from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import BookForm, SignUpForm, LoginForm
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, "list.html", {"books": books})


@login_required(login_url='login')
def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.views += 1
    book.save(update_fields=['views'])
    return render(request, "details.html", {"book": book})


@login_required(login_url='login')
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            form.save_m2m()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "form.html", {"action": "Add", "form": form})


@login_required(login_url='login')
def book_edit(request, book_id):
    book = Book.objects.get(pk=book_id)
    if book.user != request.user and not request.user.has_perm('bookstore.change_book'):
        return redirect("book_detail", book_id=book_id)
    if request.method == "POST":
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_detail", book_id=book_id)
    else:
        form = BookForm(instance=book)
    return render(request, "form.html", {"action": "Edit", "form": form})


@login_required(login_url='login')
def book_delete(request, book_id):
    book = Book.objects.get(pk=book_id)
    if book.user != request.user and not request.user.has_perm('bookstore.delete_book'):
        return redirect("book_detail", book_id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "confirm_delete.html", {"book": book})


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("book_list")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                username = User.objects.get(email=email).username
            except User.DoesNotExist:
                username = None
            user = authenticate(request, username=username, password=password) if username else None
            if user is not None:
                login(request, user)
                return redirect("book_list")
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")