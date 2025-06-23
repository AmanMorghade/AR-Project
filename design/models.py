from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    image = models.ImageField(upload_to="room/")


class Furniture(models.Model):
    name = models.CharField(max_length=255)
    model_file = models.FileField(upload_to="furniture/")

    def __str__(self):
        return self.name
    
class UserFurniture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    model_file = models.FileField(upload_to='user_furniture/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"