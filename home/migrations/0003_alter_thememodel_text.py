# Generated by Django 4.2.3 on 2023-07-21 08:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_newcategoymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thememodel',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]