# Generated by Django 2.2.7 on 2019-12-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_sub_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='sub_url',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
