# Create your models here.
from django.db import models

class ContactEntry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)  # We'll hash it before saving

    def __str__(self):
        return self.name    
