from django.db import models
from django.urls import reverse

class Data_db(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return  self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})