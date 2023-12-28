# Generated by Django 4.2.7 on 2023-12-27 19:46

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_recipe_recipe_by_alter_recipe_cropping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '300x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
