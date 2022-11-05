"""songcrud URL Configuration

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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from musicapp.views import ArtisteViewSet,SongView,LyricView

router=DefaultRouter()
router1=DefaultRouter()
router2=DefaultRouter()
router.register('',LyricView,'lyric')
router1.register('',SongView,'songs')
router2.register('',ArtisteViewSet,'artist')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('artistes/',include(router2.urls)),
    path('songs/',include(router1.urls)),
    path('lyrics/',include(router.urls))

]
