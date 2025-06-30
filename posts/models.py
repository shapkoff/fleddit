from django.db import models
from branches.models import Branch
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)

    def __str__(self):
        return self.title
    

class Image(models.Model):
    image = models.ImageField(upload_to='posts/images/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url
