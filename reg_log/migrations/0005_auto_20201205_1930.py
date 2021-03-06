# Generated by Django 3.1.2 on 2020-12-05 16:30

from django.db import migrations, models
import reg_log.models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_log', '0004_auto_20201103_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='*', max_length=50, verbose_name='Имя')),
                ('second_name', models.CharField(help_text='*', max_length=50, verbose_name='Фамилия')),
                ('third_name', models.CharField(help_text='*', max_length=50, verbose_name='Отчество')),
                ('employment_date', models.DateField(verbose_name='Дата приёма на работу')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, help_text='Формат: <em>Якуба Коласа 5, кв. 8</em>.', max_length=50, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='client',
            name='driver_license',
            field=models.CharField(help_text='*', max_length=8, unique=True, verbose_name='№ лиценции'),
        ),
        migrations.AlterField(
            model_name='client',
            name='experience',
            field=models.IntegerField(help_text='*', validators=[reg_log.models.validate_date], verbose_name='Опыт вождения'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(help_text='*', max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='patronymic',
            field=models.CharField(help_text='*', max_length=50, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(help_text='*', max_length=13, unique=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='client',
            name='surname',
            field=models.CharField(help_text='*', max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='identification_number',
            field=models.CharField(max_length=14, unique=True, verbose_name='Идентификационный номер'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='series',
            field=models.CharField(choices=[('АВ', 'АВ'), ('ВМ', 'ВМ'), ('НВ', 'НВ'), ('КН', 'КН'), ('МР', 'МР'), ('МС', 'МС'), ('КВ', 'КВ'), ('РР', 'РР')], max_length=2, verbose_name='Серия'),
        ),
    ]
