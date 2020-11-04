"""
DjangoWebProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    # Uncomment the next line to enable the admin:
    url('admin/', admin.site.urls),
    url(r'^$',include('main.urls')),
    url('catalog',include('catalog.urls')),
    url('reg_log',include('reg_log.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url('registration/', include('accounts.urls')),
    url('edit/', include('accounts.urls')),
    #url('user_cab',include('user_cab.urls')),
]