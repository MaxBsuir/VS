# Generated by Django 3.1.2 on 2020-11-03 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20201031_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='road_accident',
            name='id_service',
        ),
        migrations.AddField(
            model_name='service',
            name='id_road_accident',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.road_accident'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auto',
            name='body_type',
            field=models.CharField(choices=[('Седан', 'Седан'), ('Универсал', 'Универсал'), ('Хэтчбэк', 'Хэтчбэк'), ('Купе', 'Купе'), ('Лифтбэк', 'Лифтбэк'), ('Кроссовер', 'Кроссовер'), ('Внедорожник', 'Внедорожник')], max_length=50, verbose_name='Тип кузова'),
        ),
    ]
