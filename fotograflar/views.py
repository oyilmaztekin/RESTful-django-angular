from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from .models import FotografModel
from .serializers import FotografSerializer

#@csrf_exempt
def FotograflarView(request):
    if request.method == "GET":
        fotograf = FotografModel.objects.all()
        serializer = FotografSerializer(fotograf, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        blocked = {
            "detail":"Kayıt olusturma islemi yapılamaz"
        }
        return JsonResponse(blocked)