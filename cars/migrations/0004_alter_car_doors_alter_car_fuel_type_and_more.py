# Generated by Django 4.2.4 on 2023-08-05 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
