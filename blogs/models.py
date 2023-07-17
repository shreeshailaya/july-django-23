from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogContent(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    no_of_line = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.get(
        username='shree').pk)
    img = models.ImageField(upload_to="images/", default="default_image.png")

    def __str__(self) -> str:
        return self.title



