from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=300)
    domain = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


