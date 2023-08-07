from django import template
from ..models import BookModel, CategoryModel, ThemeModel

register = template.Library()


@register.simple_tag
def get_book():
    return BookModel.objects.all()


@register.simple_tag
def get_book_id():
    books = BookModel.objects.all()
    first_book_id = books.first().id

    return first_book_id
