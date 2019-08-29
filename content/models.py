from django.db import models
from place.models import Place
from django.contrib.auth import get_user_model

# Create your models here.

class Content(models.Model):
    site_id = models.OneToOneField(Place, on_delete=models.CASCADE)
    secondary_url = models.TextField(blank=True, max_length=300)
    html = models.TextField(blank=True)
    filter_html = models.TextField()
    qualification = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

