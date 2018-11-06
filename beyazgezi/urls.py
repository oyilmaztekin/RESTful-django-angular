"""beyazgezi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url, include
from rest_framework import routers
from .views import *
from sayfalar.views import SayfaView, SayfaDetayView
from rotalar.views import RotaView, RotaDetayView, RotaCatView, RotaCategoriesView, RotaVideoView, RotaFotoView
from iletisim.views import IletisimView
from basvur.views import BasvurView
from fotograflar.views import FotograflarView
from haberler.views import HaberView, HaberDetayView, HaberFotografView
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'api/sayfalar', SayfaViewSet)
#router.register(r'api/iletisim', IletisimView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

"""
etkinlikler > etkinlik > etkinlikfoto
fotograflar = admin panelinden eklenen tüm fotoğraflar
"""
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^beyazgezi-yonetim/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^api/sayfalar/$', SayfaView),
    url(r'^api/sayfa/(?P<pk>[0-9]+)/$', SayfaDetayView),
    url(r'^api/rotalar/$', RotaView),
    url(r'^api/rotalar/(?P<pk>[0-9]+)/$', RotaDetayView),
    url(r'^api/rotalar/videolar/(?P<pk>[0-9]+)/$', RotaVideoView),
    url(r'^api/rotalar/fotograflar/(?P<pk>[0-9]+)/$', RotaFotoView),
    url(r'^api/rotalar/kategori/(?P<pk>[0-9]+)/$', RotaCatView),
    url(r'^api/rotalar/kategoriler/$', RotaCategoriesView),
    url(r'^api/haberler/$', HaberView),
    url(r'^api/haberler/(?P<pk>[0-9]+)/$', HaberDetayView),
    url(r'^api/haberfoto/(?P<pk>[0-9]+)/$', HaberFotografView),
    url(r'^api/iletisim/$', IletisimView),
    url(r'^api/basvur/$', BasvurView),
    url(r'^api/fotograflar/$', FotograflarView),
    url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    #url(r'^', TemplateView.as_view(template_name="index.html")),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ] + urlpatterns