# Generated by Django 3.1.2 on 2020-10-31 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='body_type',
            field=models.CharField(choices=[('Седан', 'Седан'), ('Универсал', 'Универсал'), ('Хэтчбэк', 'Хэтчбэк'), ('Купе', 'Купе'), ('Лифтбэк', 'Лифтбэк')], max_length=50, verbose_name='Тип кузова'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='color',
            field=models.CharField(max_length=50, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='condition',
            field=models.BooleanField(default=True, verbose_name='Доступна'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='consumption_per_100',
            field=models.FloatField(max_length=50, verbose_name='Расход на 100 км'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='date_of_issue',
            field=models.DateField(verbose_name='Дата выпуска'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='engine',
            field=models.FloatField(max_length=50, verbose_name='Объём двигателя'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='model',
            field=models.CharField(max_length=50, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='number',
            field=models.CharField(max_length=50, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='price_per_day',
            field=models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Цена в день'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='transmission',
            field=models.CharField(choices=[('АКПП', 'АКПП'), ('МКПП', 'МКПП')], max_length=50, verbose_name='Тип КП'),
        ),
        migrations.AlterField(
            model_name='road_accident',
            name='date_road_accident',
            field=models.DateTimeField(verbose_name='Дата ДТП'),
        ),
        migrations.AlterField(
            model_name='road_accident',
            name='defect',
            field=models.CharField(max_length=500, verbose_name='Повреждения'),
        ),
        migrations.AlterField(
            model_name='service',
            name='date_of_end',
            field=models.DateTimeField(verbose_name='Дата окончания аренды'),
        ),
        migrations.AlterField(
            model_name='service',
            name='date_of_start',
            field=models.DateTimeField(verbose_name='Дата начала аренды'),
        ),
        migrations.AlterField(
            model_name='service',
            name='repair_description',
            field=models.CharField(max_length=500, verbose_name='Описание работ'),
        ),
    ]
