# Generated by Django 2.2.7 on 2019-12-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='sub_url',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
