from django.db import models
from category.models import Category
from django.urls import reverse
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField

# Create your models here.
class Project(models.Model):
    title               = models.CharField(max_length=100, unique=True)
    slug                = models.SlugField(max_length=200, unique=True)
    category            = models.ForeignKey(Category, on_delete=models.CASCADE)
    project_image       = models.ImageField(upload_to='images/projects/', null=True)
    description         = models.TextField(max_length=2000)
    created_date        = models.DateField(auto_now=True)
    framework           = models.CharField(max_length=200)
    view_link           = models.CharField(max_length=200)

    def get_url(self):
        return reverse('project_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.title


class ProjectGallery(models.Model):
    project             = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image               = models.ImageField(upload_to='images/projects/', max_length=255)

    def __str__(self):
        return self.project.title
    
    class Meta:
        verbose_name        = 'Project Gallary'
        verbose_name_plural = 'Project Gallary'