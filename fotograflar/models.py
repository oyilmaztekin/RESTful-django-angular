from django.db import models
from services.file_extentions import validate_image_extention
from beyazgezi.settings import BASE_DIR
import os

# Create your models here.
class FotografModel(models.Model):
    """Model definition for GaleriModel."""

    foto = models.ImageField(verbose_name="Fotoğraf", upload_to='uploads/fotograflar/', max_length=100, height_field=None, width_field=None, validators=[validate_image_extention])
    foto_baslik = models.CharField(verbose_name="Fotoğraf Açıklaması (Görme Engelliler için)", max_length=100, blank=True, null=True)
    olusturulma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True, verbose_name="Oluşturulma tarihi")
    guncelleme = models.DateTimeField(auto_now=True, null=True, auto_now_add=False, verbose_name="Son güncelleme", editable=False)
    
    class Meta:
        """Meta definition for FotografModel."""

        verbose_name = 'Fotoğraf'
        verbose_name_plural = 'Fotoğraflar'
    
    def image_tag(self):
        path = "/media/"+str(self.foto)
        return u'<img src="%s" style="height:80px!important;height:auto;"/>' % (path)
    
    image_tag.short_description = "Fotoğraf"
    image_tag.allow_tags = True

    def __str__(self):
        return "%s" % (self.foto_baslik)

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=FotografModel)
def fotograf_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.foto.delete(False)
