from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'cluberapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('music/', views.music, name="music"),
    path('video/', views.video, name="video"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)