from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    phone = models.CharField('Телефон', max_length=50)
    address = models.CharField('Адрес', max_length=50)
    experience = models.IntegerField('Опыт вождения')
    driver_license = models.CharField('№ лиценции', max_length=50)
    def __str__(self):
         return '{} {}'.format(self.id, self.surname)
    class Meta:
         ordering = ('id', )

class Passport(models.Model):
    client = models.OneToOneField(Client, on_delete = models.CASCADE, primary_key = True)
    series = models.CharField('Серия', max_length=50)
    identification_number = models.CharField('Идентификационный номер', max_length=50)
    def __str__(self):
         return '{}'.format(self.client)

class Account(models.Model):
    id_client = models.OneToOneField(Client, on_delete = models.CASCADE, primary_key = True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField('Почта', max_length=50)
    #password = models.CharField('Пароль', max_length=50)
    def __str__(self):
         return '{}'.format(self.id_client)