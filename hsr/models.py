from django.db import models
import psycopg2


class Product(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    picture = models.ImageField(upload_to='pictures/', verbose_name='Изображение')
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.IntegerField(verbose_name= 'Цена_за_покупку')
    date_of_creation = models.DateField(verbose_name='Датасоздания')
    last_modified_date = models.DateField(verbose_name='Датапоследнего_изменения')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return f'{self.id} {self.name} {self.price} {self.category}'


class Category(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.id} {self.name}'