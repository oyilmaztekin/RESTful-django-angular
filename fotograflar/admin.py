from django.contrib import admin
from .models import FotografModel

# Register your models here.

class FotografModelAdmin(admin.ModelAdmin):
    '''
        Admin View for 
    '''
    list_display = ('image_tag','foto','olusturulma_tarihi')
    #search_fields = ('foto_baslik','foto',)

admin.site.register(FotografModel, FotografModelAdmin)
