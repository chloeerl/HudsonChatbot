from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path to send data from frontend to the backend
    path('getResponse', views.getResponse, name='getResponse')
] 