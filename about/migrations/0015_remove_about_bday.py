# Generated by Django 4.0.4 on 2022-06-03 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0014_alter_about_bday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='bday',
        ),
    ]
