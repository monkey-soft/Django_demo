from django.db import models

# Create your models here.
class Authorform(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()