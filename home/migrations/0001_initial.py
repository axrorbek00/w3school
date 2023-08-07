# Generated by Django 4.2.3 on 2023-07-19 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.bookmodel')),
            ],
            options={
                'verbose_name': 'theme',
                'verbose_name_plural': 'themes',
            },
        ),
        migrations.CreateModel(
            name='ThemeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.categorymodel')),
            ],
            options={
                'verbose_name': 'text',
                'verbose_name_plural': 'texts',
            },
        ),
    ]
