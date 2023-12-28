from django.contrib import admin
from .models import Recipe
from image_cropping import ImageCroppingMixin
from import_export.admin import ImportExportModelAdmin


class RecipeAdmin(ImageCroppingMixin, ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Recipe, RecipeAdmin)