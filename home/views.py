from django.shortcuts import render
from .models import BookModel, CategoryModel, ThemeModel


# 127.0.0.1:8000 - Navbar
def new_category_views(request):
    return render(request, 'main/home_detail.html')


# Themes , Detail
def books_views(request, book_pk):
    form = CategoryModel.objects.filter(book_id=book_pk)  # book_id orqali Mavzular ro'yxati
    cat_id = form.first().id  # Birinchi mavzuni id sini olib beryapti
    texts = ThemeModel.objects.get(category_id=cat_id)  # Birinchi mavzu cat_id si bo'yicha detail ma'lumot olib berya-i
    return render(request, 'main/home_detail.html', context={
        'texts': texts,  # detail ma'lumot
        'books': form, # mavzular ro'yxati
        'cat_id': cat_id,  # category id

    })


# Detail , Themes
def text_views(request, category_pk):
    texts = ThemeModel.objects.get(category_id=category_pk)  # Bu category_pk ga biriktirilgan Theme ni detail
    category_id = category_pk
    bk_id = CategoryModel.objects.get(id=category_pk).book_id  # Bu category_pk ga biriktirilgan book_id ni olib beradi.
    form = CategoryModel.objects.all().filter(book_id=bk_id)  # book_id orqali Mavzular ro'yxagi
    return render(request, 'main/home_detail.html', context={
        'texts': texts,  # detail ma'lumot
        'books': form,  # mavzular ro'yxati
        'cat_id': category_id,  # category id
    })
