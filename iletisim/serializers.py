from .models import IletisimModel
from rest_framework import serializers



#class SayfaSerializer(serializers.HyperlinkedModelSerializer):
class IletisimSerializer(serializers.ModelSerializer):
    class Meta:
        model = IletisimModel
        fields = "__all__"