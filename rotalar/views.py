from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from .models import RotalarModel, KategoriModel
from .videoModel import RotaVideoModel
from .photoModel import RotaFotografModel
from .serializers import RotaSerializer, KategoriSerializer, RotaVideoSerializer, RotaFotografSerializer

#@csrf_exempt
def RotaView(request):
    if request.method == "GET":
        rotalar = RotalarModel.objects.exclude(is_passive__isnull=True).order_by("-olusturulma_tarihi")
        serializer = RotaSerializer(rotalar, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        blocked = {
            "detail":"Kayıt olusturma islemi yapılamaz"
        }
        return JsonResponse(blocked)

#@csrf_exempt
def RotaDetayView(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        rotalar = RotalarModel.objects.get(pk=pk)
    except RotalarModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RotaSerializer(rotalar)
        return JsonResponse(serializer.data)


#@csrf_exempt
def RotaCategoriesView(request):
    if request.method == "GET":
        kategoriler = KategoriModel.objects.all().order_by("-olusturulma_tarihi")
        serializer = KategoriSerializer(kategoriler, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        blocked = {
            "detail":"Kayıt olusturma islemi yapılamaz"
        }
        return JsonResponse(blocked)

#@csrf_exempt
def RotaCatView(request, pk):
    print(pk)
    if request.method == "GET":
        rotalar = RotalarModel.objects.all().filter(parent=pk).order_by("-olusturulma_tarihi")
        serializer = RotaSerializer(rotalar, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        blocked = {
            "detail":"Kayıt olusturma islemi yapılamaz"
        }
        return JsonResponse(blocked)

def RotaFotoView(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        fotograflar = RotaFotografModel.objects.filter(gezi_id=pk)
    except RotalarModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RotaFotografSerializer(fotograflar, many=True)
        return JsonResponse(serializer.data, safe=False)

    else:
        blocked = {
            "detail":"Kayıt olusturma islemi yapılamaz"
        }
        return JsonResponse(blocked)


def RotaVideoView(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        videolar = RotaVideoModel.objects.filter(gezi_id=pk)
    except RotalarModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RotaVideoSerializer(videolar, many=True)
        return JsonResponse(serializer.data, safe=False)

    else:
        blocked = {
            "detail":"Kayıt olusturma islemi yapılamaz"
        }
        return JsonResponse(blocked)