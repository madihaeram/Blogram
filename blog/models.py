from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    #status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')])

    def __str__(self):
        return self.title

