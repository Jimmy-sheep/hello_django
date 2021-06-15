from django.db import models

# Create your models here.
class API(models.Model):
    id = models.PositiveIntegerField(blank=True)
    title = models.CharField(max_length=100)
    classify = models.CharField(max_length=100)
    descrption = models.TextField(blank=True)
    picture = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    poblish = models.BooleanField(blank=True)
