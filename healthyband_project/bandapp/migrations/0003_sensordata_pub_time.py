# Generated by Django 4.2.2 on 2024-01-26 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bandapp', '0002_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='pub_time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
