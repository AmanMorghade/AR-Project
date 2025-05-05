from django.db import models

# Create your models here.

class Room(models.Model):
    image = models.ImageField(upload_to="room/")


class Furniture(models.Model):
    name = models.CharField(max_length=255)
    model_file = models.FileField(upload_to="furniture/")

    def __str__(self):
        return self.name