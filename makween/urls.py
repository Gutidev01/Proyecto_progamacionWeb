from django.urls import path
from . import views
from django.urls import path


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index', views.index, name='index'),
    path('mision-vision', views.mision_vision, name='mision-vision'),
    path('formulario', views.formulario, name='formulario'),
    path('galeria', views.galeria, name='galeria'),
    path('sucursal', views.sucursal, name='sucursal'),
    path('base', views.producto_list, name='base'),
    path('detail/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('create/', views.producto_create, name='producto_create'),
    path('update/<int:pk>/', views.producto_update, name='producto_update'),
    path('delete/<int:pk>/', views.producto_delete, name='producto_delete'),
]

