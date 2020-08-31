from django.urls import path

from . import views

urlpatterns = [
    path('telusko',views.index,name='index')
]