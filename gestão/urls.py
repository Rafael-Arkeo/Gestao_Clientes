"""gestão URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from gestão.settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import clientes.url as clientes_urls
from django.contrib.auth import views as views_auth
from home import urls as home_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include(clientes_urls)),
    path('login/', views_auth.LoginView.as_view(), name='login'),
    path('', include(home_urls)),
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)




