from django.db import models

class Post(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    CATEGORY_CHOICES = [
    ('nature', 'Nature Related'),
    ('health', 'Health Related'),
    ('tech', 'Tech Related'),]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='tech')
    def __str__(self):
        return self.title

