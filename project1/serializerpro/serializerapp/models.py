from django.db import models

# Create your models here.
class Comment(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created = models.DateField()
    email = models.EmailField()
