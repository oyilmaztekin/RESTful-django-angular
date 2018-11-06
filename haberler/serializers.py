from .models import HaberModel
from .photoModel import HaberFotografModel
from rest_framework import serializers
import locale


locale.setlocale(locale.LC_TIME, "tr_TR")

class HaberSerializer(serializers.ModelSerializer):
    #fotos = FotoListingField(many=True)
    class Meta:
        model = HaberModel
        fields = "__all__"

class HaberFotografSerializer(serializers.ModelSerializer):
    #fotos = FotoListingField(many=True)
    class Meta:
        model = HaberFotografModel
        fields = "__all__"
