from django.db import migrations
from registration import models

def create_categories(apps, schema_editor):
    '''создание категорий'''
    category_model = apps.get_model('registration', 'Category')
    for category_choice in models.Category.CATEGORIES_CHOICES:
        category_model(name=category_choice[0]).save()

def remove_categories(apps, schema_editor):
    '''удаление категорий'''
    category_model = apps.get_model('registration', 'Category')
    for category_choice in models.Category.CATEGORIES_CHOICES:
        category_model.objects.get(name=category_choice[0]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_categories, reverse_code=remove_categories),
    ]
