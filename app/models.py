from django.db import models
from pyexpat import model

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

