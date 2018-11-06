from django.db import models
from .models import RotalarModel

# Create your models here.
class RotaVideoModel(models.Model):
    video_url = models.CharField(verbose_name="Video Bağlantısı", max_length=200, blank=True, null=True)
    gezi = models.ForeignKey(RotalarModel, on_delete=models.CASCADE, related_name="gezi_video")
    olusturulma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True, verbose_name="Oluşturulma tarihi")
    guncelleme = models.DateTimeField(auto_now=True, null=True, auto_now_add=False, verbose_name="Son güncelleme", editable=False)
    
    class Meta:
        verbose_name = 'Gezi Videoları'
        verbose_name_plural = 'Gezi Videoları'
    
    def __str__(self):
        self.olusturulma_tarihi = self.olusturulma_tarihi
        self.guncelleme = self.guncelleme
        return "%s" % (self.video_url)