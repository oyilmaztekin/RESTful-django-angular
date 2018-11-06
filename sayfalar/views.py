from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from .models import SayfaModel
from .serializers import SayfaSerializer

#@csrf_exempt
def SayfaView(request):
    if request.method == "GET":
        sayfalar = SayfaModel.objects.exclude(is_passive__isnull=True).order_by("-olusturulma_tarihi")
        serializer = SayfaSerializer(sayfalar, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        blocked = {
            "detail":"Kayıt olusturma islemi yapılamaz"
        }
        return JsonResponse(blocked)

#@csrf_exempt
def SayfaDetayView(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        sayfalar = SayfaModel.objects.get(pk=pk)
    except SayfaModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SayfaSerializer(sayfalar)
        return JsonResponse(serializer.data)