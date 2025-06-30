from django.db import models
from branches.models import Branch
from django.contrib.auth import get_user_model

# Create your models here.
class Following(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id}: {self.branch_id}'
