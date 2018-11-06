from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import IletisimModel
from .serializers import IletisimSerializer
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
from django.views.decorators.csrf import csrf_protect
#from ratelimit.decorators import ratelimit

#@ratelimit(key='ip', method=ratelimit.UNSAFE)
#@ratelimit(key='ip', rate='2/m', block=True)
@api_view(['POST'])
@csrf_protect
def IletisimView(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        serializer = IletisimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # kime = serializer.data['ad_soyad']
            # mail = serializer.data['email']
            # mail_temsilci = 'yilmaztekin.ozer@gmail.com'
            # mail_mesaj = serializer.data['mesaj']

            # if mail != "":			
            #     #smtp ayarları
            #     sender = "BEYAZMASA"
            #     receivers = mail, mail_temsilci
            #     author = formataddr((str(Header(u'Websitesi İletişim Kutusu', 'utf-8')), "yilmaztekin.ozer@gmail.com"))			
            #     message = MIMEMultipart('alternative')
            #     message['From'] = author
            #     message = """From: %s\nSubject: [Websitesi iletişim kutusu]: \n\n %s Mesajınız başarıyla kaydedilmiştir. \n """ % (author, kime)			
            #     smtpObj = smtplib.SMTP('smtp.gmail.com:587')
            #     #smtpObj = smtplib.SMTP('mail.ibb.gov.tr:587')
            #     user = 'yilmaztekin.ozer@gmail.com'			
            #     password = 'zulcelalh8i1p8r1'		
            #     smtpObj.ehlo()
            #     smtpObj.starttls()
            #     smtpObj.login(user, password)
            #     smtpObj.sendmail(sender, receivers, message)
            #     smtpObj.quit()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        blocked = {
            "detail":"Forbidden"
        }
        return JsonResponse(blocked)
