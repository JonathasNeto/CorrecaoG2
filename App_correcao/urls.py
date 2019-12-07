from django.urls import path
from . import views

urlpatterns = [
    path('',views.lista,name='solicitação'),
    path('lista/',views.cargo,name='lista'),
    path('solicitar/',views.solicitar,name='Solicitar')
]