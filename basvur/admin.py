from django.contrib import admin
from .models import BasvurModel

# Register your models here.
class BasvurModelAdmin(admin.ModelAdmin):
    '''
        Admin View for IletisimModel
    '''
    list_display = ('ad_soyad','gezi_turu','basvuru_turu','gelis_tarihi', 'gelis_tarihi',)
    #search_fields = ('ad_soyad','email',)
    list_filter = ('gezi_turu','basvuru_turu',)
    readonly_fields = ('email','mesaj','ad_soyad', 'tel_no', 'gezi_turu', 'basvuru_turu', 'gelis_tarihi', 'gelis_tarihi',)




admin.site.register(BasvurModel, BasvurModelAdmin)


# Register your models here.
