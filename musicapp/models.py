from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    age=models.IntegerField(max_lenght=50)

    def __str__(self) :
        return self.first_name

class Song(models.Model):
    title=models.CharField(max_length=200)
    date_released=models.DateField()
    likes=models.IntegerField()
    artist_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self) :
         return self.title

class Lyric(models.Model):
    content=models.CharField(_MAX_LENGTH=500)
    song_id=models.ForeignKey(Song,on_delete=models.CASCADE)
