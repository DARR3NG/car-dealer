from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.


class Car (TranslatableModel):
    state_choice= (('Tanger-Tétouan-Al Hoceïma', 'Tanger-Tétouan-Al Hoceïma'),
    ('L\'Oriental', 'L\'Oriental'),
    ('Fès-Meknès', 'Fès-Meknès'),
    ('Rabat-Salé-Kénitra', 'Rabat-Salé-Kénitra'),
    ('Béni Mellal-Khénifra', 'Béni Mellal-Khénifra'),
    ('Casablanca-Settat', 'Casablanca-Settat'),
    ('Marrakech-Safi', 'Marrakech-Safi'),
    ('Drâa-Tafilalet', 'Drâa-Tafilalet'),
    ('Souss-Massa', 'Souss-Massa'),
    ('Guelmim-Oued Noun', 'Guelmim-Oued Noun'),
    ('Laâyoune-Sakia El Hamra', 'Laâyoune-Sakia El Hamra'),
    ('Dakhla-Oued Ed-Dahab', 'Dakhla-Oued Ed-Dahab'))

    year_choice= []
    for r in range(2000,(datetime.now().year+1)):
            year_choice.append((r,r))
    

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    translations=TranslatedFields(
    

    color = models.CharField( _("color"),max_length=100,null=True),

    condition = models.CharField(_("condition"),max_length=100,null=True ),
    
    description = RichTextField(_("description"),null=True),

    
    
    
    transmission = models.CharField(_("transmission"),max_length=100,null=True),
    interior = models.CharField(_("interior"),max_length=100,null=True),
    
    
    
    
    fuel_type = models.CharField(_("fuel_type"),max_length=50,null=True),

    )
    car_title = models.CharField(_("car_title"),max_length=255 ,null=True)
    vin_no = models.CharField(_("vin_no"),max_length=100,null=True)
    state = models.CharField(_("state"),choices=state_choice, max_length=100,null=True)
    city = models.CharField( _("city"),max_length=100,null=True)
    model = models.CharField(_("model"),max_length=100 ,null=True)
    year = models.IntegerField(_("year"),choices=year_choice,null=True)
    engine = models.CharField(_("engine"),max_length=100,null=True)
    doors = models.CharField( _("doors"),choices=door_choices, max_length=100,null=True)
    passengers = models.IntegerField(_("passengers"),null=True)
    price = models.IntegerField(_("price"),null=True)
    car_photo=models.ImageField(_("car_photo"),upload_to='photos/%Y/%m/%d/',null=True)
    car_photo_1 = models.ImageField(_("car_photo_1"),upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(_("car_photo_2"),upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(_("car_photo_3 "),upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(_("car_photo_4"),upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(_("features"),choices=features_choices, max_length=255,null=True)
    body_style = models.CharField( _("body_style"),max_length=100,null=True)
    

    
   
    
    
    

    
    

    miles = models.IntegerField(_("miles"),null=True)
    milage = models.IntegerField(_("milage"),null=True)
    no_of_owners = models.CharField(_("no_of_owners"),max_length=100,null=True)
    is_featured = models.BooleanField(_("is_featured"),default=False)
    created_at=models.DateTimeField(_('created_date'),auto_now_add=True,blank=True,null=True)

    """
    car_title=models.CharField(max_length=255)
    state=models.CharField(choices=state_choice,max_length=100)
    city=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    year=models.IntegerField(('year'),choices=year_choice)
    condition=models.CharField(max_length=100)
    price=models.IntegerField()
    description=RichTextField()
    car_photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    car_photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    car_photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    car_photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    features=MultiSelectField(choices=features_choices,max_length=255)
    body_style=models.CharField(max_length=100)
    engine=models.CharField(max_length=100)
    transmission=models.CharField(max_length=100)
    interior=models.CharField(max_length=100)
    miles=models.IntegerField()
    doors=models.CharField(choices=door_choices,max_length=100)
    passengers=models.IntegerField()
    vin_no=models.CharField(max_length=100)
    milage=models.IntegerField()
    fuel_type=models.CharField(max_length=50)
    no_of_owners=models.CharField(max_length=100)
    is_featured=models.BooleanField(default=False)
    """
  

    def __str__(self):
        return self.car_title
    
