# Generated by Django 2.1.2 on 2018-10-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_and_chapters', '0004_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
