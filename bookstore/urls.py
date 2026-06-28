from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
    path("books/add/", views.book_create, name="book_create"),
    path("books/<int:book_id>/edit/", views.book_edit, name="book_edit"),
    path("books/<int:book_id>/delete/", views.book_delete, name="book_delete"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]