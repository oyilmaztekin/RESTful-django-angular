from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from .models import HaberModel
from .photoModel import HaberFotografModel
from .serializers import HaberSerializer, HaberFotografSerializer

#@csrf_exempt
def HaberView(request):
    if request.method == "GET":
        haberler = HaberModel.objects.all()
        serializer = HaberSerializer(haberler, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        blocked = {
            "detail":"Kayıt olusturma islemi yapılamaz"
        }
        return JsonResponse(blocked)

#@csrf_exempt
def HaberDetayView(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        haberler = HaberModel.objects.get(pk=pk)
    except HaberModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HaberSerializer(haberler)
        return JsonResponse(serializer.data)
    else:
        blocked = {
            "detail":"Kayıt olusturma islemi yapılamaz"
        }
        return JsonResponse(blocked)


"""
Fotoğraflar etkinlik id sine göre listeleniyor. Önce etkinlik sorgusuyla etkinlik id sini alıyoruz. 
Sonra etkinlik id sini fotoğraf sorgusuna gönderiyoruz. Etkinlik id sine bağlı fotolar listeleniyor. 
"""
#@csrf_exempt
def HaberFotografView(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        fotograflar = HaberFotografModel.objects.filter(haber_id=pk)
    except HaberModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HaberFotografSerializer(fotograflar, many=True)
        return JsonResponse(serializer.data, safe=False)

    else:
        blocked = {
            "detail":"Kayıt olusturma islemi yapılamaz"
        }
        return JsonResponse(blocked)