# Generated by Django 4.2.2 on 2024-01-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
                ('heartPulse', models.IntegerField(default=0)),
                ('dhtTemp', models.IntegerField(default=0)),
                ('dhtHum', models.IntegerField(default=0)),
                ('gyroX', models.FloatField(default=0)),
                ('gyroY', models.FloatField(default=0)),
                ('gyroZ', models.FloatField(default=0)),
                ('acceleroX', models.FloatField(default=0)),
                ('acceleroY', models.FloatField(default=0)),
                ('acceleroZ', models.FloatField(default=0)),
            ],
        ),
    ]