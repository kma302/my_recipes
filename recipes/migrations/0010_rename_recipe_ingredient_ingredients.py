# Generated by Django 4.2.6 on 2023-12-08 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_ingredient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='recipe',
            new_name='ingredients',
        ),
    ]