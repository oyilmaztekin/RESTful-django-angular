from .models import FotografModel
from rest_framework import serializers
import locale


locale.setlocale(locale.LC_TIME, "tr_TR")
#class SayfaSerializer(serializers.HyperlinkedModelSerializer):
class FotografSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotografModel
        fields = "__all__"