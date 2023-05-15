from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    # La función __str__ define cómo se mostrará el objeto Post en la consola de Django.
