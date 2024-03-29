"""lunch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
import stores.urls
from stores.views import store_list, store_detail, StoreViewSet
from pages.views import home

router = DefaultRouter()
router.register(r'store', StoreViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^store/', include('stores.urls')),
]
