from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True) # slug is a part of a URL which identifies a particular page on a website in a form readable by users