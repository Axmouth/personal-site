# Generated by Django 3.0.3 on 2020-02-17 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='project_image',
            field=models.ImageField(default='', upload_to='documents/%Y/%m/%d/'),
        ),
    ]
