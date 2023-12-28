# Generated by Django 4.2.7 on 2023-12-27 17:42

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_alter_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_by',
            field=models.CharField(default='Karen Arthur', max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '200x200', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
