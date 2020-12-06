from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_date(value):
    if value <= 1 or value >= 50:
        raise ValidationError('%s Введите корректное значение' % value)

SERIES = (
        ('АВ', 'АВ'),
        ('ВМ', 'ВМ'),
        ('НВ', 'НВ'),
        ('КН', 'КН'),
        ('МР', 'МР'),
        ('МС', 'МС'),
        ('КВ', 'КВ'),
        ('РР', 'РР'),
    )

class Client(models.Model):
    surname = models.CharField('Фамилия', max_length=50, null=False)
    name = models.CharField('Имя', max_length=50, null=False)
    patronymic = models.CharField('Отчество', max_length=50, null=False)
    series = models.CharField('Серия', max_length=2, choices=SERIES)
    identification_number = models.CharField('Идентификационный номер', max_length=14, unique=True)
    driver_license = models.CharField('№ лицензии', max_length=8, unique=True)
    experience = models.IntegerField('Опыт вождения', validators=[validate_date], help_text="Формат: <em>от 2 до 49</em>.", null=False)
    phone = models.CharField('Телефон', max_length=13, unique=True)
    email = models.EmailField('Почта', max_length=50, unique=True, blank=True, null=True)
    address = models.CharField('Адрес', max_length=50 , blank=True, null=True, help_text="Формат: <em>Якуба Коласа 5, кв. 8</em>.")
    def __str__(self):
         return '{}'.format(self.id)
    class Meta:
         ordering = ('id', )

#class Passport(models.Model):
#    client = models.OneToOneField(Client, on_delete = models.CASCADE, primary_key = True)
#    series = models.CharField('Серия', max_length=2, choices=SERIES)
#    identification_number = models.CharField('Идентификационный номер', max_length=14, unique=True)
#    def __str__(self):
#         return '{}'.format(self.client)
#    class Meta:
#         ordering = ('client', )

class Employee(models.Model):
    second_name = models.CharField('Фамилия', max_length=50, null=False)
    first_name = models.CharField('Имя', max_length=50, null=False)    
    third_name = models.CharField('Отчество', max_length=50, null=False)
    employment_date = models.DateField('Дата приёма на работу')
    def __str__(self):
         return '{} {}'.format(self.id, self.first_name)
    class Meta:
         ordering = ('id', )