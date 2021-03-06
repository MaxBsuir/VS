# Generated by Django 3.1.2 on 2020-10-30 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_start', models.DateTimeField()),
                ('date_of_end', models.DateTimeField()),
                ('repair_description', models.CharField(max_length=500)),
                ('id_auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.auto')),
            ],
        ),
        migrations.CreateModel(
            name='Road_Accident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_road_accident', models.DateTimeField()),
                ('defect', models.CharField(max_length=500)),
                ('id_auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.auto')),
                ('id_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.service')),
            ],
        ),
    ]
