from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def validate_date(value):
    if value <= 1 or value >= 50:
        raise ValidationError('%s Введите корректное значение' % value)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    patronymic = models.CharField('Отчество', max_length=50, help_text="*")
    experience = models.IntegerField('Опыт вождения', validators=[validate_date], help_text="*", null=False)
    driver_license = models.CharField('№ лицензии', max_length=8, unique=True, help_text="*")
    phone = models.CharField('Телефон', max_length=13, unique=True, help_text="*")
    address = models.CharField('Адрес', max_length=50 , blank=True, null=True, help_text="Формат: <em>Якуба Коласа 5, кв. 8</em>.")
    date_of_birth = models.DateField('Дата рождения', blank=True, null=True, help_text="Формат: <em>ГГГГ-ММ-ДД</em>.")

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

#class Passport(models.Model):
#    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
#    series = models.CharField('Серия', max_length=7, unique=True, blank=True, null=True)
#    identification_number = models.CharField('Идентификационный номер', max_length=7, unique=True, blank=True, null=True)

#    def __str__(self):
#         return '{}'.format(self.user)




#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()