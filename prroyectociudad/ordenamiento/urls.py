from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_parroquia_barrio, name='inicio'), 
    path('listar_barrios/', views.listar_barrios, name='listar_barrios'),
    path('crear_parroquia/', views.crear_parroquia, name='crear_parroquia'),
    path('crear_barrio/', views.crear_barrio, name='crear_barrio'),
]
