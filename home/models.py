from django.db import models
from ckeditor.fields import RichTextField

class NewCategoyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    book_name = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'


class CategoryModel(models.Model):
    theme_name = models.CharField(max_length=100)
    book = models.ForeignKey(BookModel, on_delete=models.RESTRICT)

    def __str__(self):
        return self.theme_name

    class Meta:
        verbose_name = 'theme'
        verbose_name_plural = 'themes'


class ThemeModel(models.Model):
    text = RichTextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'text'
        verbose_name_plural = 'texts'
