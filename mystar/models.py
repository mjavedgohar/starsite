from django.db import models

class BlogPost(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  # Add other fields as needed (e.g., author, publish date)
