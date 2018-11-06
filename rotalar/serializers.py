from .models import RotalarModel, KategoriModel
from .videoModel import RotaVideoModel
from .photoModel import RotaFotografModel
from rest_framework import serializers
import locale


locale.setlocale(locale.LC_TIME, "tr_TR")
#class SayfaSerializer(serializers.HyperlinkedModelSerializer):
class RotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotalarModel
        fields = "__all__"


class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriModel
        fields = "__all__"

class RotaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotaVideoModel
        fields = "__all__"

class RotaFotografSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotaFotografModel
        fields = "__all__"