from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who posted the tweet
    text = models.TextField(max_length=240)  # Text content of the tweet (max 240 characters)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)  # Optional image upload
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when tweet was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when tweet was last updated

    def __str__(self):
        return f'{self.user.username} - {self.text[:20]}'
