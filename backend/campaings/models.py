from django.db import models

# Create your models here.
class Campaing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    slug = models.SlugField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    # We will be saving the images in Cloudinary
    
    