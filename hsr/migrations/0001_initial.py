# Generated by Django 4.1.5 on 2023-01-20 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('picture', models.ImageField(upload_to='pictures/', verbose_name='Изображение')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена_за_покупку')),
                ('date_of_creation', models.DateField(verbose_name='Датасоздания')),
                ('last_modified_date', models.DateField(verbose_name='Датапоследнего_изменения')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
    ]
