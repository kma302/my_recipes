# Generated by Django 5.0 on 2023-12-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, upload_to='recipe_images'),
        ),
    ]
