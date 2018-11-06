from django.contrib import admin
from .models import RotalarModel, KategoriModel
from .photoModel import RotaFotografModel
from .videoModel import  RotaVideoModel

class FotografInline(admin.TabularInline):
    model = RotaFotografModel

class VideoInline(admin.TabularInline):
    model = RotaVideoModel

class RotalarModelAdmin(admin.ModelAdmin):
    inlines = (
        FotografInline,
        VideoInline,
    )
    list_display = ('baslik','parent', 'is_passive', 'olusturulma_tarihi', 'guncelleme',)
    list_filter = ('parent','is_passive')
    exclude = ('olusturulma_tarihi',)
    search_fields = ('baslik','parent')
    

class KategoriModelAdmin(admin.ModelAdmin):
    '''
        Admin View for KategoriModel
    '''
    list_display = ('baslik', 'olusturulma_tarihi', 'guncelleme',)
    exclude = ('olusturulma_tarihi',)
    search_fields = ('baslik',)


admin.site.register(KategoriModel, KategoriModelAdmin)
admin.site.register(RotalarModel, RotalarModelAdmin)
# Register your models here.

