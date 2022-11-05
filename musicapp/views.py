
from operator import imod
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Artiste,Song,Lyric
from .serializer import ArtisteSerializer,SongSerializer,LyricSerializer
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
# Create your views here.

class ArtisteViewSet(viewsets.ModelViewSet):
    serializer_class=ArtisteSerializer
    queryset=Artiste.objects.all()

class SongView(viewsets.ModelViewSet):
    serializer_class=SongSerializer
    queryset=Song.objects.all()
  
class LyricView(viewsets.ModelViewSet):
    serializer_class=LyricSerializer
    queryset=Lyric.objects.all()






   
