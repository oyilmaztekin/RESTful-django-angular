from .models import SayfaModel
from rest_framework import serializers
import locale


locale.setlocale(locale.LC_TIME, "tr_TR")
#class SayfaSerializer(serializers.HyperlinkedModelSerializer):
class SayfaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SayfaModel
        fields = "__all__"