from django.utils.html import format_html
from django.contrib import admin
from .models import Car
from parler.admin import TranslatableAdmin

# Register your models here.

class CarAdmin(TranslatableAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width = "40px" style="border-radius:100px" />'.format(object.car_photo.url))
    
    thumbnail.short_description='Car Image'
    list_display=('id','thumbnail','car_title','city','color','model','year','body_style','fuel_type','is_featured')
    list_display_links=('id','thumbnail','car_title')
    list_editable=('is_featured',)
    search_fields=('id','car_title','city','model','body_style','translations__fuel_type')
    list_filter=('city','model','body_style','translations__fuel_type')
    fields=('car_title','state','city','color','model','year','condition','price','description','car_photo','car_photo_1','car_photo_2','car_photo_3','car_photo_4','features','body_style','engine','transmission','interior','miles','doors','passengers','vin_no','milage','fuel_type','no_of_owners','is_featured')

admin.site.register(Car,CarAdmin)
