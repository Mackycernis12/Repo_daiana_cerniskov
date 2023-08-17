"""
URL configuration for libreria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("principal" ,views.inicio, name="principal"),
    path("alta_usuarios", views.registrar_empleados, name="alta_users"),
    path("alta_clientes", views.registrar_clientes, name="alta_clientes"),
    path("alta_libros", views.alta_libros, name="alta_libros"),
    path("buscar_libros",views.buscar_libros, name="buscar_libros"),
    path("buscar", views.buscar)
]
