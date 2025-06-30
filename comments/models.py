from django.db import models
from posts.models import Post
from django.contrib.auth import get_user_model

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=500)
    user = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
