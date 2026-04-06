from django.db import models
from django.contrib.auth.models import User 


class Artist(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.artist.name}" 
    
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.user}" 