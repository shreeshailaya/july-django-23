from django.db import models

# Create your models here.

class BlogContent(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    no_of_line = models.IntegerField()
    img = models.ImageField(upload_to="images/", default="images/default_image.png")

    def __str__(self) -> str:
        return self.title



