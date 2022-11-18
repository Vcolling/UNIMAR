"""CURSO URL Configuration

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
from UNIMAR import views
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Pessoa/all/', views.listar_pessoas),
    path('Pessoa/detalhe_pessoa/<id>/', views.detalhe_pessoas),
    path('Pessoa/registro/', views.cadastro_pessoa),
    path('Pessoa/registro/submit', views.alterar_pessoa),
    path('Pessoa/registro/delete/<id>/', views.deletar_pessoa),
    path('', TemplateView.as_view(template_name="index.html"))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
