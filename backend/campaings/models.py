from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# Create your models here.
class Campaing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    slug = models.SlugField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    # We will be saving the images in Cloudinary
    image = CloudinaryField('Image', overwrite=True, format='jpg')
    
    class Meta:
        verbose_name = 'Campaing'
        verbose_name_plural = 'Campaings'
        ordering = ('-created',)
    
    def save(self, **args):
        title = self.title
        to_assign = slugify(title)
        
        # We need the slug to be unique (could have put the unique to title)
        if Campaing.objects.filter(slug=to_assign).exists():
            # We append at the end the number of items that exist
            counter = Campaing.objects.filter(slug=to_assign).count()
            to_assign = to_assign + '_' + counter
            
        self.slug = to_assign
        self.save()
    
    def __str__(self):
        return self.title

class Suscriber(models.Model):
    # Link the suscriber to the campaing
    campaing = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Suscriber'
        verbose_name_plural = 'Suscribers'
        ordering = ('-subscribed_at',)
    
    def __str__(self):
        return self.email
    