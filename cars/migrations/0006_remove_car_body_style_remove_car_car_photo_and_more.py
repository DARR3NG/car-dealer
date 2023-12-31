# Generated by Django 4.2.4 on 2023-09-29 14:43

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_description_alter_car_doors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='body_style',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_photo',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_photo_1',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_photo_2',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_photo_3',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_photo_4',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_title',
        ),
        migrations.RemoveField(
            model_name='car',
            name='city',
        ),
        migrations.RemoveField(
            model_name='car',
            name='color',
        ),
        migrations.RemoveField(
            model_name='car',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='car',
            name='description',
        ),
        migrations.RemoveField(
            model_name='car',
            name='doors',
        ),
        migrations.RemoveField(
            model_name='car',
            name='engine',
        ),
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
        migrations.RemoveField(
            model_name='car',
            name='fuel_type',
        ),
        migrations.RemoveField(
            model_name='car',
            name='interior',
        ),
        migrations.RemoveField(
            model_name='car',
            name='is_featured',
        ),
        migrations.RemoveField(
            model_name='car',
            name='milage',
        ),
        migrations.RemoveField(
            model_name='car',
            name='miles',
        ),
        migrations.RemoveField(
            model_name='car',
            name='model',
        ),
        migrations.RemoveField(
            model_name='car',
            name='no_of_owners',
        ),
        migrations.RemoveField(
            model_name='car',
            name='passengers',
        ),
        migrations.RemoveField(
            model_name='car',
            name='price',
        ),
        migrations.RemoveField(
            model_name='car',
            name='state',
        ),
        migrations.RemoveField(
            model_name='car',
            name='transmission',
        ),
        migrations.RemoveField(
            model_name='car',
            name='vin_no',
        ),
        migrations.RemoveField(
            model_name='car',
            name='year',
        ),
        migrations.CreateModel(
            name='CarTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('car_title', models.CharField(max_length=255, verbose_name='Titre de la voiture')),
                ('state', models.CharField(choices=[('Tanger-Tétouan-Al Hoceïma', 'Tanger-Tétouan-Al Hoceïma'), ("L'Oriental", "L'Oriental"), ('Fès-Meknès', 'Fès-Meknès'), ('Rabat-Salé-Kénitra', 'Rabat-Salé-Kénitra'), ('Béni Mellal-Khénifra', 'Béni Mellal-Khénifra'), ('Casablanca-Settat', 'Casablanca-Settat'), ('Marrakech-Safi', 'Marrakech-Safi'), ('Drâa-Tafilalet', 'Drâa-Tafilalet'), ('Souss-Massa', 'Souss-Massa'), ('Guelmim-Oued Noun', 'Guelmim-Oued Noun'), ('Laâyoune-Sakia El Hamra', 'Laâyoune-Sakia El Hamra'), ('Dakhla-Oued Ed-Dahab', 'Dakhla-Oued Ed-Dahab')], max_length=100, verbose_name='État')),
                ('city', models.CharField(max_length=100, verbose_name='Ville')),
                ('color', models.CharField(max_length=100, verbose_name='Couleur')),
                ('model', models.CharField(max_length=100, verbose_name='Modèle')),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], verbose_name='Année')),
                ('condition', models.CharField(max_length=100, verbose_name='Condition')),
                ('price', models.IntegerField(verbose_name='Prix')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('car_photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo de la voiture')),
                ('car_photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo de la voiture 1')),
                ('car_photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo de la voiture 2')),
                ('car_photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo de la voiture 3')),
                ('car_photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo de la voiture 4')),
                ('features', multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=255, verbose_name='Fonctionnalités')),
                ('body_style', models.CharField(max_length=100, verbose_name='Style de carrosserie')),
                ('engine', models.CharField(max_length=100, verbose_name='Moteur')),
                ('transmission', models.CharField(max_length=100, verbose_name='Transmission')),
                ('interior', models.CharField(max_length=100, verbose_name='Intérieur')),
                ('miles', models.IntegerField(verbose_name='Kilométrage')),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=100, verbose_name='Nombre de portes')),
                ('passengers', models.IntegerField(verbose_name='Nombre de passagers')),
                ('vin_no', models.CharField(max_length=100, verbose_name='Numéro de VIN')),
                ('milage', models.IntegerField(verbose_name='Consommation')),
                ('fuel_type', models.CharField(max_length=50, verbose_name='Type de carburant')),
                ('no_of_owners', models.CharField(max_length=100, verbose_name='Nombre de propriétaires')),
                ('is_featured', models.BooleanField(default=False, verbose_name='En vedette')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='cars.car')),
            ],
            options={
                'verbose_name': 'car Translation',
                'db_table': 'cars_car_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
