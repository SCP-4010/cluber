from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=120, default="Unknown")
    icon = models.ImageField(upload_to="icons/", default="")

class Music(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    mp3 = models.FileField(upload_to='mp3/')

class Video(models.Model):
    properties = models.OneToOneField(Music, on_delete=models.CASCADE, primary_key=True)
    url = models.CharField(max_length=120)