from django.db import models

# Create your models here. This is a db table
class Article(models.Model):  #this class inherites from models.Model
  title = models.CharField(max_length=100)
  slug = models.SlugField()
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  #thumbnail
  #author
  #slug
