from django.db import models
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Data_db.Status.PUB)

class Data_db(models.Model):
    class Status(models.IntegerChoices):
        DR = 0, 'Черновик'
        PUB = 1, 'Опубликовано'

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUB)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    objects = models.Manager()
    Published_manager = PublishedManager()

    cat = models.ForeignKey('Category_db', on_delete=models.PROTECT)

    def __str__(self):
        return  self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    

class Category_db(models.Model):
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name