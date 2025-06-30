from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=50)                  # fl/<name>
    title = models.CharField(max_length=100)                # title of branch
    description = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='branches/images/', default='branches/images/default_logo.png')

    def __str__(self):
        return self.name
