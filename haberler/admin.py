from django.contrib import admin
from .photoModel import HaberFotografModel
from .models import HaberModel


class FotografInline(admin.TabularInline):
    model = HaberFotografModel


class HaberModelAdmin(admin.ModelAdmin):
    inlines = (
        FotografInline,
    )
    list_display = ('baslik','olusturulma_tarihi','guncelleme',)
    # search_fields = ('icerik','baslik')
    readonly_fields = ('slug',)
    

admin.site.register(HaberModel, HaberModelAdmin)