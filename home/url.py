from django.urls import path
from .views import new_category_views, books_views, text_views

urlpatterns = [
    path('', new_category_views, name='new_category'),
    path('book/<int:book_pk>/', books_views, name='books'),   # book_id
    path('text/<int:category_pk>/', text_views, name='text')   # category_id
]
