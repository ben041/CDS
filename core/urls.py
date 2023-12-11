from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView



urlpatterns = [
    path('', views.index, name='home-page'),
    path('chatbot', views.Bot, name='bot041'),
    path('databot.json', RedirectView.as_view(url=staticfiles_storage.url('databot.json'))),
    path('dio/ai/', views.Dio, name='dio_ai'),
    path('disease_detection', views.disease_detection, name='disease_detection'),
    path('vitualisation/<int:pk>', views.view_district, name='district_d')
    
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



