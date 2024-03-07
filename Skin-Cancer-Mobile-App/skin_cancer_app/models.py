from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


def user_directory_path(instance, filename):
    return 'images/{0}/'.format(filename)


class SkinImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images', default='posts/default.jpg')
