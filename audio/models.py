from django.db import models
import datetime

class audio(models.Model):
    name = models.CharField(max_length=100, unique=True)
    audio_file = models.FileField(upload_to='media/uploads', null=False)
    genre = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(default=datetime.datetime.now)
