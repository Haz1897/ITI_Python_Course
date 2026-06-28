from django.contrib import admin
from .models import Book, Category, ISBN


class ISBNInline(admin.StackedInline):
    model = ISBN
    extra = 0
    readonly_fields = ('isbn_number',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rate', 'views', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'rate', 'categories')
    filter_horizontal = ('categories',)
    inlines = [ISBNInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ISBN)
class ISBNAdmin(admin.ModelAdmin):
    list_display = ('isbn_number', 'book_title', 'author_title', 'book')
    search_fields = ('isbn_number', 'book_title', 'author_title')
    readonly_fields = ('isbn_number',)