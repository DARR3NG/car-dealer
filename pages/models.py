from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

class Team(TranslatableModel):

    translations=TranslatedFields(
        first_name=models.CharField(_('first_name'),max_length=255),
        last_name=models.CharField(_('last_name'),max_length=255),
        designation=models.CharField(_('designation'),max_length=255),

    )

    photo=models.ImageField(_('photo'),upload_to='photos/%Y/%m/%d/')
    facebook_link=models.URLField(_('facebook_link'),max_length=100)
    twitter_link=models.URLField(_('twitter_link'),max_length=100)
    google_plus_link=models.URLField(_('google_plus_link'),max_length=100)
    created_date=models.DateTimeField(_('created_date'),auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name
        


