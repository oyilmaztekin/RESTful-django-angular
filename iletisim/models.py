from django.db import models
from django.utils.text import slugify
import datetime

# Create your models here.

class IletisimModel(models.Model):
    """Model definition for IletisimModel."""
    ad_soyad = models.CharField(verbose_name="Adı Soyadı", max_length=120)
    email = models.EmailField(verbose_name="Email", max_length=254)
    mesaj = models.TextField(verbose_name="Mesajınız")
    gelis_tarihi = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Son güncelleme", editable=False, blank=True, null=True)
    

    class Meta:
        """Meta definition for IletisimModel."""

        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim Mesajları'

    def __str__(self):
        """Unicode representation of IletisimModel."""
        return "%s" % (self.ad_soyad)