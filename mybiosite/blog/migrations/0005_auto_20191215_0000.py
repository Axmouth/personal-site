# Generated by Django 2.2.7 on 2019-12-14 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191213_1313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Blog Post', 'verbose_name_plural': 'Blog Posts'},
        ),
    ]
