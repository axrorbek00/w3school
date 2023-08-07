from django.contrib import admin
from .models import BookModel, CategoryModel, ThemeModel, NewCategoyModel


# Register your models here.


class ThemeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']


class BookModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name']


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'theme_name', 'book']


admin.site.register(ThemeModel, ThemeModelAdmin)
admin.site.register(BookModel, BookModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)
