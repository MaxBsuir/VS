from django.db import models
from django.conf import settings

def validate_date(value):
    if value <= 0:
        raise ValidationError('%s Введите корректное значение' % value)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    #name = models.CharField('Имя', max_length=50)
    #surname = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField(max_length=50)
    #phone = models.CharField('Телефон', max_length=50, unique=True)
    #address = models.CharField('Адрес', max_length=50)
    #experience = models.IntegerField('Опыт вождения', validators=[validate_date])
    #driver_license = models.CharField('№ лиценции', max_length=50, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)