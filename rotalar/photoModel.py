from django.db import models
from services.file_extentions import validate_image_extention
from .models import RotalarModel

# Create your models here.
class RotaFotografModel(models.Model):
    """Model definition for GaleriModel."""

    foto = models.ImageField(verbose_name="Fotoğraf", upload_to='uploads/haberler/', max_length=100, height_field=None, width_field=None, validators=[validate_image_extention], blank=True, null=True)
    foto_baslik = models.CharField(verbose_name="Fotoğraf Açıklaması (Görme Engelliler için)", max_length=100, blank=True, null=True)
    foto_url = models.URLField(verbose_name="İmaj Bağlantısı", max_length=200, blank=True, null=True)
    gezi = models.ForeignKey(RotalarModel, on_delete=models.CASCADE, related_name="gezi_foto")
    olusturulma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True, verbose_name="Oluşturulma tarihi")
    guncelleme = models.DateTimeField(auto_now=True, null=True, auto_now_add=False, verbose_name="Son güncelleme", editable=False)
    
    class Meta:
        """Meta definition for FotografModel."""

        verbose_name = 'Gezi Fotoğrafı'
        verbose_name_plural = 'Gezi Fotoğrafları'

    
    def __str__(self):
        self.olusturulma_tarihi = self.olusturulma_tarihi
        self.guncelleme = self.guncelleme
        return "%s" % (self.foto_baslik)

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=RotaFotografModel)
def fotograf_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.foto.delete(False)