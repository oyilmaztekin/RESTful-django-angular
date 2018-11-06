# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from django.utils.text import slugify
from services.file_extentions import validate_image_extention

# Create your models here.
class HaberModel(models.Model):
    """Model definition for HaberModel."""
    baslik = models.CharField(verbose_name="Başlık", max_length=120)
    icerik = HTMLField(verbose_name="İçerik veya Açıklama", blank=True, null=True)
    foto = models.ImageField(verbose_name="Fotoğraf", upload_to='uploads/egitimler/', max_length=100, height_field=None, width_field=None, validators=[validate_image_extention], blank=True, null=True)
    olusturulma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True, verbose_name="Oluşturulma tarihi")
    guncelleme = models.DateTimeField(auto_now=True, null=True, auto_now_add=False, verbose_name="Son güncelleme", editable=False)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        """Meta definition for HaberModel."""

        verbose_name = 'Haber'
        verbose_name_plural = 'Haberler'
    
    def save(self, *args, **kwargs):
        if not self.baslik:
            if not self.slug:
                self.slug = slugify(str(self.olusturulma_tarihi)+'-'+str(self.id))
                super(HaberModel, self).save(*args, **kwargs) # Call the real save() method
        
        if self.baslik:
            if not self.slug:
                slug_title = str(self.baslik+'-'+str(self.id))
                self.slug = slugify(slug_title)
                super(HaberModel, self).save(*args, **kwargs) # Call the real save() method"""
            super(HaberModel, self).save(*args, **kwargs) # Call the real save() method"""
        
    def __str__(self):
        """Str representation of HaberModel."""
        return "%s - %s" % (self.baslik, self.slug)
