# Generated by Django 4.1.5 on 2023-01-20 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hsr', '0002_category_created_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_add',
        ),
    ]
