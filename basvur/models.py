from django.db import models
from django.utils.text import slugify
import datetime
from services.file_extentions import validate_excel_extention

# Create your models here.

class BasvurModel(models.Model):
    gezi_turu = models.CharField(verbose_name="Gezi Türü", max_length=120) #gezi türlerine kategorilere query gönder.
    basvuru_turu = models.CharField(verbose_name="Bavuru Türü", max_length=120, default="Sosyal Geziler")
    ad_soyad = models.CharField(verbose_name="Ad Soyad", max_length=120)
    tel_no = models.CharField(verbose_name="Telefon Numarası", max_length=11, default="05555555555",)
    email = models.EmailField(verbose_name="Email", max_length=254)
    mesaj = models.TextField(verbose_name="Mesajınız")
    gelis_tarihi = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Son güncelleme", editable=False, blank=True, null=True)
    

    class Meta:
        """Meta definition for IletisimModel."""

        verbose_name = 'Başvuru'
        verbose_name_plural = 'Başvurular'

    def __str__(self):
        """Unicode representation of IletisimModel."""
        return "%s" % (self.ad_soyad)