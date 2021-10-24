from django.db import models


class Registration(models.Model):
    '''Регистрация'''
    STATUS_SUCCESS = 'SUCCESS'
    STATUS_ERROR = 'ERROR'
    STATUSES_CHOICES = (
        (STATUS_SUCCESS, 'Успешно'),
        (STATUS_ERROR, 'Ошибка'),
    )
    created = models.DateTimeField(
        verbose_name='Время и дата создания',
        auto_now_add=True
    )
    vehicle = models.ForeignKey(
        verbose_name='Транспорт',
        to='registration.Vehicle',
        related_name='registrations',
        on_delete=models.CASCADE,
        null=True,
    )
    row_number = models.CharField(
        verbose_name='Первоначальный номер',
        max_length=50,
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=7,
        choices=STATUSES_CHOICES,
        default=STATUS_ERROR,
    )
    message = models.CharField(
        verbose_name='Сообщение',
        max_length=250,
    )


class Vehicle(models.Model):
    '''Транспорт'''
    number = models.CharField(
        verbose_name='Номер',
        max_length=10
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to='registration.Category', 
        related_name='vehicles',
        on_delete=models.SET_NULL,
        null=True,
    )
    

class Category(models.Model):
    '''Категория'''
    CATEGORY_A = 'А'
    CATEGORY_B = 'В'
    CATEGORY_C = 'С'
    CATEGORIES_CHOICES = (
        (CATEGORY_A, 'А'),
        (CATEGORY_B, 'В'),
        (CATEGORY_C, 'С'),
    )
    name = models.CharField(
        verbose_name='Название', 
        max_length=1,
        choices=CATEGORIES_CHOICES, 
        default=CATEGORY_A,
    )
