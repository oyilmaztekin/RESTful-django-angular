from .models import BasvurModel
from rest_framework import serializers



#class SayfaSerializer(serializers.HyperlinkedModelSerializer):
class BasvurSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasvurModel
        fields = "__all__"