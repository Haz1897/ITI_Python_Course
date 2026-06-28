from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, ISBN


@receiver(post_save, sender=Book)
def create_isbn_for_book(sender, instance, created, **kwargs):
    if created:
        ISBN.objects.create(
            book=instance,
            author_title=instance.user.get_full_name() or instance.user.username,
            book_title=instance.title,
        )