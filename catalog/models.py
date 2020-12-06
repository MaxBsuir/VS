from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

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
        ('Внедорожник', 'Внедорожник'),
        ('Родстер', 'Родстер'),
    )
    FUEL_TYPE = (
        ('Бензин', 'Бензин'),
        ('Дизель', 'Дизель'),
        ('Гибрид', 'Гибрид'),
    )
    COLOR = (
        ('Красный', 'Красный'),
        ('Синий', 'Синий'),
        ('Чёрный', 'Чёрный'),
        ('Зеленый', 'Зеленый'),
        ('Серый', 'Серый'),
        ('Белый', 'Белый'),
        ('Оранжевый', 'Оранжевый'),
        ('Жёлтый', 'Жёлтый'),
        ('Коричневый', 'Коричневый'),
    )
    BRAND=(
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Chevrolet', 'Chevrolet'),
        ('Citroen', 'Citroen'),
        ('Ford', 'Ford'),
        ('Geely', 'Geely'),
        ('Honda', 'Honda'),
        ('Hyundai', 'Hyundai'),
        ('Kia', 'Kia'),
        ('LADA', 'LADA'),
        ('Lexus', 'Lexus'),
        ('Mazda', 'Mazda'),
        ('Mercedec-Benz', 'Mercedec-Benz'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Nissan', 'Nissan'),
        ('Opel', 'Opel'),
        ('Peugeot', 'Peugeot'),
        ('Range Rover', 'Range Rover'),
        ('Renault', 'Renault'),
        ('Skoda', 'Skoda'),
        ('Toyota', 'Toyota'),
        ('Volkswagen', 'Volkswagen'),
        ('Volvo', 'Volvo'),
    )
    PLACES=(
        ('2', '2'),
        ('4', '4'),
        ('5', '5'),
        ('7', '7'),
    )
    brand = models.CharField('Марка', max_length=50, choices=BRAND)
    model = models.CharField('Модель', max_length=50)
    body_type = models.CharField('Тип кузова', max_length=50, choices=BODY_TYPE)
    number = models.CharField('Номер', max_length=5, unique=True)
    date_of_issue = models.DateField('Дата выпуска')
    color = models.CharField('Цвет', max_length=50, choices=COLOR)
    engine = models.FloatField('Объём двигателя (л.)', max_length=50, validators=[validate_even])
    transmission = models.CharField('Тип КП', max_length=50, choices=TRANSMISSION)
    consumption_per_100 = models.FloatField('Расход (на 100 км.)', max_length=50, validators=[validate_even])
    price_per_day = models.DecimalField('Цена в день (Br)', max_digits=18, decimal_places=2, validators=[validate_even])
    condition = models.BooleanField('Доступна', default=True)
    reserve = models.CharField('Запас хода (км.)', max_length=5)
    places = models.CharField('Места', max_length=2, choices=PLACES)
    capacity = models.CharField('Багажник (л.)', max_length=5)
    fuel = models.CharField('Топливо', max_length=50, choices=FUEL_TYPE)
    power = models.CharField('Мощность (л.с.)', max_length=4)
    foto = models.ImageField('Фото', upload_to='catalog/')
   # def __str__(self):
       # template = '{0.id} {0.brand} {0.model}'
        #return template.format(self)
    def get_absolute_url(self):
         return reverse('carsingle',
                      args=[self.id])
    def __str__(self):
         return '{}, {}, {}'.format(self.id, self.brand, self.number)


class Road_Accident(models.Model):
    id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)    
    #id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    #id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    date_road_accident = models.DateField('Дата ДТП')
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