from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from services.file_extentions import validate_image_extention

# Create your models here.

class SayfaModel(models.Model):
    """Model definition for SayfaModel."""
    baslik = models.CharField(verbose_name="Sayfa Adı", max_length=50)
    #icerik = RichTextField(verbose_name="İçerik", blank=True, null=True )
    icerik = HTMLField(verbose_name="İçerik", blank=True, null=True )
    foto = models.ImageField(verbose_name="Fotoğraf", upload_to='uploads/sayfalar/', max_length=100, height_field=None, width_field=None, validators=[validate_image_extention], blank=True, null=True)
    #foto_url = models.URLField(verbose_name="Fotoğraf Bağlantısı(eğer dışarıdan eklenecekse", max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Kategori")
    is_passive = models.BooleanField(verbose_name="Aktif")
    olusturulma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True, verbose_name="Oluşturulma tarihi")
    guncelleme = models.DateTimeField(auto_now=True, null=True, auto_now_add=False, verbose_name="Son güncelleme", editable=False)
    

    class Meta:
        """Meta definition for SayfaModel."""

        verbose_name = 'Sayfa'
        verbose_name_plural = 'Sayfalar'

    def __str__(self):
        """Unicode representation of SayfaModel."""
        return "%s" % (self.baslik)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_title = str(self.baslik+'-'+str(self.id))
            self.slug = slugify(slug_title)
            super(SayfaModel, self).save(*args, **kwargs) # Call the real save() method"""
        
        super(SayfaModel, self).save(*args, **kwargs)
        
