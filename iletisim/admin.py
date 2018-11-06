from django.contrib import admin
from .models import IletisimModel

# Register your models here.

class IletisimModelAdmin(admin.ModelAdmin):
    '''
        Admin View for IletisimModel
    '''
    list_display = ('ad_soyad','email','mesaj','gelis_tarihi')
    #search_fields = ('ad_soyad','email',)
    readonly_fields = ('ad_soyad', 'email', 'mesaj','gelis_tarihi',)

admin.site.register(IletisimModel, IletisimModelAdmin)
