# models.py
from django.db import models

class Church(models.Model):
    name = models.CharField(max_length=100,default='Your default address here')
    denomination = models.CharField(max_length=100,default='Your default address here')
    address = models.CharField(max_length=255, default='Your default address here')
    phone = models.CharField(max_length=15,default='Your default address here')
    email = models.EmailField(default='Your default address here')

class FileModel(models.Model):
    file = models.FileField(upload_to='files/')

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

