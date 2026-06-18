from django.db import models

class Book(models.Model):
    title = models.CharField("Book Title", max_length=255, unique=True)
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