from django.db import models
from django.contrib.auth.models import User
from posts.models import Post



class Review(models.Model):
    """
    Review model, related to Post.
    User can write a review of the event and 
    leave a star (1-5) rating of that event.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.TextField()
    rating = models.IntegerField()

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f"{self.owner}'s review"