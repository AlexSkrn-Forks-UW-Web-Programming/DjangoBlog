"""This module defines Python classes/Django models for our blog system."""

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Define the main Python class for our blog system, a Post."""

    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    # A single author can have many posts, while each post has only one author.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    """Define a class to represent categories our blog posts may fall into."""

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    # Any given Post might belong in more than one Category
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
