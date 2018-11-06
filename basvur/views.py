from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BasvurModel
from .serializers import BasvurSerializer
from django.views.decorators.csrf import csrf_protect

#from ratelimit.decorators import ratelimit

#@ratelimit(key='ip', method=ratelimit.UNSAFE)
#@ratelimit(key='ip', rate='2/m', block=True)
@api_view(['POST'])
@csrf_protect
def BasvurView(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        serializer = BasvurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        blocked = {
            "detail":"Forbidden"
        }
        return JsonResponse(blocked)
