# Generated by Django 4.2.4 on 2023-09-29 16:05

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_remove_car_created_at_delete_cartranslation'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Car Photo'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Car Photo 1'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Car Photo 2'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Car Photo 3 '),
        ),
        migrations.AddField(
            model_name='car',
            name='car_photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Car Photo 4'),
        ),
        migrations.AddField(
            model_name='car',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='car',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date'),
        ),
        migrations.AddField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=100, null=True, verbose_name='Doors'),
        ),
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.CharField(max_length=100, null=True, verbose_name='Engine'),
        ),
        migrations.AddField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=255, null=True, verbose_name='Features'),
        ),
        migrations.AddField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False, null=True, verbose_name='Is Featured'),
        ),
        migrations.AddField(
            model_name='car',
            name='milage',
            field=models.IntegerField(null=True, verbose_name='Milage'),
        ),
        migrations.AddField(
            model_name='car',
            name='miles',
            field=models.IntegerField(null=True, verbose_name='Miles'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=100, null=True, verbose_name='Model'),
        ),
        migrations.AddField(
            model_name='car',
            name='no_of_owners',
            field=models.CharField(max_length=100, null=True, verbose_name='No of Owners'),
        ),
        migrations.AddField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(null=True, verbose_name='Passengers'),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('Tanger-Tétouan-Al Hoceïma', 'Tanger-Tétouan-Al Hoceïma'), ("L'Oriental", "L'Oriental"), ('Fès-Meknès', 'Fès-Meknès'), ('Rabat-Salé-Kénitra', 'Rabat-Salé-Kénitra'), ('Béni Mellal-Khénifra', 'Béni Mellal-Khénifra'), ('Casablanca-Settat', 'Casablanca-Settat'), ('Marrakech-Safi', 'Marrakech-Safi'), ('Drâa-Tafilalet', 'Drâa-Tafilalet'), ('Souss-Massa', 'Souss-Massa'), ('Guelmim-Oued Noun', 'Guelmim-Oued Noun'), ('Laâyoune-Sakia El Hamra', 'Laâyoune-Sakia El Hamra'), ('Dakhla-Oued Ed-Dahab', 'Dakhla-Oued Ed-Dahab')], max_length=100, null=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='car',
            name='vin_no',
            field=models.CharField(max_length=100, null=True, verbose_name='Vin No'),
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], null=True, verbose_name='Year'),
        ),
        migrations.CreateModel(
            name='CarTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('car_title', models.CharField(max_length=255, null=True, verbose_name='Car Title')),
                ('color', models.CharField(max_length=100, null=True, verbose_name='Color')),
                ('condition', models.CharField(max_length=100, null=True, verbose_name='condition')),
                ('description', ckeditor.fields.RichTextField(null=True, verbose_name='Designation')),
                ('body_style', models.CharField(max_length=100, null=True, verbose_name='Body Style')),
                ('transmission', models.CharField(max_length=100, null=True, verbose_name='transmission')),
                ('interior', models.CharField(max_length=100, null=True, verbose_name='Interior')),
                ('fuel_type', models.CharField(max_length=50, null=True, verbose_name='Fuel Type')),
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