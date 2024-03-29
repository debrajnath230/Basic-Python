from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return self.title