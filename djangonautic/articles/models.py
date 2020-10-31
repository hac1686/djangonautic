from django.db import models

# Create your models here. This is a db table
class Article(models.Model):  #this class inherites from models.Model
  title = models.CharField(max_length=100)
  slug = md
  body
  date
  #thumbnail
  #author
  #slug
