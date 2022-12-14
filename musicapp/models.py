
from django.db import models
from datetime import datetime
# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50, primary_key = True)
    date_released = models.DateField() #default= datetime.today()
    likes = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.title}"

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
    
    content = models.CharField(max_length = 1000)
    
    
    
    
    
'''
class Artiste(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    date_released = models.DateField() #default= datetime.today()
    likes = models.PositiveIntegerField()
    # artiste_id = models.CharField()  #auto_created = True, primary_key = True  
    
    def __str__(self):
        return f"{self.title}"

class Lyric(models.Model):
    # song = models.ForeignKey(Song, on_delete = models.CASCADE)
    song_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    # song_id = models.CharField(max_length = 50)
    content = models.CharField(max_length = 1000)
    
  '''  