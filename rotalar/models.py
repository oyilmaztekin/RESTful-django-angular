from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from services.file_extentions import validate_image_extention
# Create your models here.

class RotalarModel(models.Model):
    baslik = models.CharField(verbose_name="Sayfa Adı", max_length=50)
    #icerik = RichTextField(verbose_name="İçerik", blank=True, null=True )
    icerik = HTMLField(verbose_name="İçerik", blank=True, null=True )
    foto = models.ImageField(verbose_name="Fotoğraf", upload_to='uploads/rotalar/', max_length=100, height_field=None, width_field=None, validators=[validate_image_extention], blank=True, null=True)
    #foto_url = models.CharField(verbose_name="Fotoğraf Bağlantısı(eğer dışarıdan eklenecekse", max_len#foto_url = models.CharField(verbose_name="Fotoğraf Bağlantısı(eğer dışarıdan eklenecekse", max_length=200, blank=True, null=True)gth=200, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    parent = models.ForeignKey('KategoriModel', related_name='kategori', on_delete=models.CASCADE, verbose_name="Kategori")
    is_passive = models.BooleanField(verbose_name="Pasif")
    olusturulma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True, verbose_name="Oluşturulma tarihi")
    guncelleme = models.DateTimeField(auto_now=True, null=True, auto_now_add=False, verbose_name="Son güncelleme", editable=False)
    class Meta:
        verbose_name='Rota'
        verbose_name_plural = 'Rotalar'

    def __str__(self):
    	return "%s" % (self.baslik)

    def __repr__(self):
    	return "%s" % (self.baslik)

    def save(self, *args, **kwargs):
    	if not self.slug:
    		slug_title = str(self.baslik+'-'+str(self.id))
    		self.slug = slugify(slug_title)
    		super(RotalarModel, self).save(*args, **kwargs)

    	super(RotalarModel, self).save(*args, **kwargs)

class KategoriModel(models.Model):
    baslik = models.CharField(verbose_name="Sayfa Adı", max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)
    olusturulma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True, verbose_name="Oluşturulma tarihi")
    guncelleme = models.DateTimeField(auto_now=True, null=True, auto_now_add=False, verbose_name="Son güncelleme", editable=False)
    
    class Meta:
        verbose_name = 'Rota Kategorisi'
        verbose_name_plural = 'Rota Kategorileri'

    def __str__(self):
        return "%s" % (self.baslik)

    def __repr__(self):
        return "%s" % (self.baslik)
	
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_title = str(self.baslik+'-'+str(self.id))
            self.slug = slugify(slug_title)
            super(KategoriModel, self).save(*args, **kwargs)
        super(KategoriModel, self).save(*args, **kwargs)
