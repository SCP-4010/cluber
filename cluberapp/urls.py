from django.urls import path
from . import views

app_name = 'cluberapp'

urlpatterns = [
    path('', views.index, name="name"),
]
