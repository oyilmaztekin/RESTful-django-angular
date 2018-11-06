from django.contrib import admin
from .models import SayfaModel
from fotograflar.models import FotografModel

class SayfaModelAdmin(admin.ModelAdmin):
    '''
        Admin View for SayfaModel
    '''

    list_display = ('baslik','parent', 'is_passive', 'slug', 'olusturulma_tarihi', 'guncelleme',)
    #list_filter = ('parent','is_passive')
    exclude = ('olusturulma_tarihi',)
    #search_fields = ('baslik','parent')

admin.site.register(SayfaModel, SayfaModelAdmin)


# Register your models here.
