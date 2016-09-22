from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamps = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamps", "-updated"]