from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from django.template import RequestContext
from django.shortcuts import render
from ratelimit.decorators import ratelimit
from rotalar.models import RotalarModel
from haberler.models import HaberModel
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@ratelimit(key='ip', method=ratelimit.ALL)
@ratelimit(key='ip', rate='50000/h', block=True)
def index(request):
    rotalar = RotalarModel.objects.all().order_by("-olusturulma_tarihi") 
    haberler = HaberModel.objects.all().order_by("-olusturulma_tarihi")[:4] 
    context += RequestContext(request)
    context = {
        "rotalar":rotalar,
        "haberler":haberler
    }
    template = "index.html"
    return render(request, template, context)