from django.db import models
from email.mime import image

# Create your models here.
class Profile(models.Model):
    full_name       = models.CharField(max_length=100)
    profession      = models.CharField(max_length=100)
    profile_pic     = models.ImageField(upload_to='images/profile/', null=True)
    description     = models.TextField(max_length=500, blank=True)
    email           = models.EmailField(max_length=200, unique=True, blank=True)
    number          = models.CharField(max_length=50, blank=True)
    linkedin        = models.CharField(max_length=200, unique=True, blank=True)
    facebook        = models.CharField(max_length=200, unique=True, blank=True)
    twitter         = models.CharField(max_length=200, unique=True, blank=True)
    instagram       = models.CharField(max_length=200, unique=True, blank=True)
    cv              = models.FileField(upload_to='files/', null=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name        = 'Profile'
        verbose_name_plural = 'Profile'

