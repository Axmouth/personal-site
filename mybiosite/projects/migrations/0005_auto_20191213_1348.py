# Generated by Django 2.2.7 on 2019-12-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20191213_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='technologies_used',
            field=models.ManyToManyField(related_name='projects', to='projects.Technology'),
        ),
    ]
