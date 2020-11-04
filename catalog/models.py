from django.db import models
from django.core.exceptions import ValidationError

def validate_even(value):
    if value <= 0:
        raise ValidationError('%s Введите корректное значение' % value)

class Auto(models.Model):   
    TRANSMISSION = (
        ('АКПП', 'АКПП'),
        ('МКПП', 'МКПП'),
    )
    BODY_TYPE = (
        ('Седан', 'Седан'),
        ('Универсал', 'Универсал'),
        ('Хэтчбэк', 'Хэтчбэк'),
        ('Купе', 'Купе'),
        ('Лифтбэк', 'Лифтбэк'),
        ('Кроссовер', 'Кроссовер'),
        ('Внедорожник', 'Внедорожник'),
    )
    brand = models.CharField('Марка', max_length=50)
    model = models.CharField('Модель', max_length=50)
    body_type = models.CharField('Тип кузова', max_length=50, choices=BODY_TYPE)
    number = models.CharField('Номер', max_length=50, unique=True)
    date_of_issue = models.DateField('Дата выпуска')
    color = models.CharField('Цвет', max_length=50)
    engine = models.FloatField('Объём двигателя', max_length=50, validators=[validate_even])
    transmission = models.CharField('Тип КП', max_length=50, choices=TRANSMISSION)
    consumption_per_100 = models.FloatField('Расход на 100 км', max_length=50, validators=[validate_even])
    price_per_day = models.DecimalField('Цена в день', max_digits=18, decimal_places=2, validators=[validate_even])
    condition = models.BooleanField('Доступна', default=True)
   # def __str__(self):
       # template = '{0.id} {0.brand} {0.model}'
        #return template.format(self)
    def __str__(self):
         return '{} {}'.format(self.id, self.brand)


class Road_Accident(models.Model):
    id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)    
    #id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    #id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    date_road_accident = models.DateTimeField('Дата ДТП')
    defect = models.TextField('Повреждения')
    def __str__(self):
         return '{}'.format(self.id)

class Service(models.Model):
    id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    id_road_accident = models.ForeignKey(Road_Accident, on_delete=models.CASCADE)
    date_of_start = models.DateTimeField('Дата начала ремонта')
    date_of_end = models.DateTimeField('Дата окончания ремонта')
    repair_description = models.TextField('Описание работ')
    def __str__(self):
         return '{}'.format(self.id)
    def save(self, *args, **kwargs):
        if(self.date_of_end > self.date_of_start):
            super(Service, self).save(*args, **kwargs)
        else:
            raise Exception("Время окончания ремонта не может быть раньше времени начала ремонта")