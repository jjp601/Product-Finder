from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    icon = models.ImageField(upload_to='images/', blank=True)
    url = models.URLField(max_length=250, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=1)
    founder = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name