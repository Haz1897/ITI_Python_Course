from django.db import migrations

DEFAULT_CATEGORIES = [
    "Fiction",
    "Non-Fiction",
    "Science",
    "Technology",
    "History",
    "Biography",
    "Self-Help",
    "Fantasy",
    "Mystery",
    "Romance",
]

def seed_categories(apps, schema_editor):
    Category = apps.get_model('bookstore', 'Category')
    for name in DEFAULT_CATEGORIES:
        Category.objects.get_or_create(name=name)

def unseed_categories(apps, schema_editor):
    Category = apps.get_model('bookstore', 'Category')
    Category.objects.filter(name__in=DEFAULT_CATEGORIES).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_categories, unseed_categories),
    ]