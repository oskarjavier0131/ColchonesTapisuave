from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalog, name='catalog'),
    path('colchon/<slug:slug>/', views.mattress_detail, name='mattress_detail'),
    path('categoria/<slug:slug>/', views.category_detail, name='category_detail'),
    path('descargar-catalogo/', views.download_catalog, name='download_catalog'),
]