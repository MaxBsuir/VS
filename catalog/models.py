from django.db import models

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
    )
    brand = models.CharField('Марка', max_length=50)
    model = models.CharField('Модель', max_length=50)
    body_type = models.CharField('Тип кузова', max_length=50, choices=BODY_TYPE)
    number = models.CharField('Номер', max_length=50)
    date_of_issue = models.DateField('Дата выпуска')
    color = models.CharField('Цвет', max_length=50)
    engine = models.FloatField('Объём двигателя', max_length=50)
    transmission = models.CharField('Тип КП', max_length=50, choices=TRANSMISSION)
    consumption_per_100 = models.FloatField('Расход на 100 км', max_length=50)
    price_per_day = models.DecimalField('Цена в день', max_digits=18, decimal_places=2)
    condition = models.BooleanField('Доступна', default=True)
   # def __str__(self):
       # template = '{0.id} {0.brand} {0.model}'
        #return template.format(self)
    def __str__(self):
         return '{}'.format(self.id)

class Service(models.Model):
    id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    date_of_start = models.DateTimeField('Дата начала аренды')
    date_of_end = models.DateTimeField('Дата окончания аренды')
    repair_description = models.TextField('Описание работ')
    def __str__(self):
         return '{}'.format(self.id)

class Road_Accident(models.Model):
    id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    id_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    #id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    #id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    date_road_accident = models.DateTimeField('Дата ДТП')
    defect = models.TextField('Повреждения')
    def __str__(self):
         return '{}'.format(self.id)