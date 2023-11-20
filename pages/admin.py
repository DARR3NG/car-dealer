from django.contrib import admin

from pages.models import Team
from django.utils.html import format_html
from parler.admin import TranslatableAdmin
# Register your models here.

class TeamAdmin(TranslatableAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width = "40px" style="border-radius:100px" />'.format(object.photo.url))
    
    thumbnail.short_description='image'

    list_display= ('id','thumbnail','first_name','last_name','designation','created_date')
    list_display_links=('id','last_name','first_name')
    search_fields=('first_name','last_name','designation')
    list_filter=('translations__designation',)
    fields = ('first_name','last_name','designation','photo','facebook_link','twitter_link',
              'google_plus_link')

admin.site.register(Team,TeamAdmin)



