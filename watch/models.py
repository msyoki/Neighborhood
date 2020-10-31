from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profilepic/',default='default.jpeg')
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    bio= models.CharField(max_length=250)
    email=models.EmailField()

    def __str__(self):
        return self.first_name
    