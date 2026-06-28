import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_title_length(value):
    if len(value) < 10:
        raise ValidationError("Book title must be at least 10 characters long.")
    if len(value) > 50:
        raise ValidationError("Book title must be no more than 50 characters long.")


def validate_category_name(value):
    if len(value) < 2:
        raise ValidationError("Category name must be at least 2 characters long.")


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[validate_category_name])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    categories = models.ManyToManyField(Category, related_name="books")
    title = models.CharField("Book Title", max_length=50, unique=True, validators=[validate_title_length])
    description = models.TextField("Book Description")
    rate = models.PositiveIntegerField(default=0)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Title: {self.title}"

    class Meta:
        ordering = ['created_at']
        verbose_name = "Book Model"
        verbose_name_plural = "Books"
        db_table = "books"


class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name="isbn")
    author_title = models.CharField("Author Title", max_length=255)
    book_title = models.CharField("Book Title", max_length=255)
    isbn_number = models.CharField("ISBN Number", max_length=17, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.isbn_number:
            self.isbn_number = self._generate_isbn()
        super().save(*args, **kwargs)

    def _generate_isbn(self):
        digits = ''.join(random.choices(string.digits, k=12))
        groups = [digits[:3], digits[3:5], digits[5:8], digits[8:11], digits[11]]
        return '-'.join(groups)

    def __str__(self):
        return f"ISBN {self.isbn_number} — {self.book_title}"

    class Meta:
        verbose_name = "ISBN"
        verbose_name_plural = "ISBNs"
        db_table = "isbns"