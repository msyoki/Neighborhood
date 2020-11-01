from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Neighborhood(models.Model):
    name=models.CharField(max_length=40)
    location=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profilepic/',default='default.jpeg')
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    bio= models.CharField(max_length=250)
    email=models.EmailField()
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name
