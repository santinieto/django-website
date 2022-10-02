"""myWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from appWebsite import views

urlpatterns = [
    path("admin/",                                                      admin.site.urls),
    path("http-index/",                                                 views.httpIndex,                name = 'http_index'),
    path("http-inicio/",                                                views.httpIndex,                name = 'http_inicio'),
    path("index/",                                                      views.index,                    name = 'index'),
    path("inicio/",                                                     views.index,                    name = 'inicio'),
    path("hola-mundo/",                                                 views.holaMundo,                name = 'hola_mundo'),
    path("pagina-generica/",                                            views.paginaGenerica,           name = 'pagina_generica'),
    path("calculadora-years/",                                          views.calculadoraYears,         name = 'calculadora_years'),
    path("contacto/",                                                   views.contacto,                 name = 'contacto'),
    path("http-crear-articulo/",                                        views.httpCrearArticulo,        name = 'http_crear_articulo'),
    path("http-crear-articulo/<str:title>",                             views.httpCrearArticulo,        name = 'http_crear_articulo'),
    path("http-crear-articulo/<str:title>/<str:content>",               views.httpCrearArticulo,        name = 'http_crear_articulo'),
    path("http-crear-articulo/<str:title>/<str:content>/<str:public>",  views.httpCrearArticulo,        name = 'http_crear_articulo'),
    path("crear-articulo/",                                             views.crearArticulo,            name = 'crear_articulo'),
    path("crear-articulo-clase/",                                       views.crearArticuloClase,       name = 'crear_articulo_clase'),
    path("obtener-articulo/",                                           views.getArticulo,              name = 'obtener_articulo'),
    path("editar-articulo/",                                            views.editArticulo,             name = 'editar_articulo'),
    path("mostrar-articulos/",                                          views.mostrarArticulos,         name = 'mostrar_articulos'),
    path("borrar-articulo/<int:id>",                                    views.borrarArticulo,           name = 'borrar_articulo'),
]