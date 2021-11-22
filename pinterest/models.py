from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # following = models.ForeignKey('self', null=True,related_name='followedBy',on_delete=models.CASCADE)

    followers = models.ManyToManyField(
        to='self',
        related_name='followees',
        symmetrical=False
    )

    def __str__(self):
        return self.username
# Create your models here.

class Pin(models.Model):
    title= models.CharField(max_length=50)
    alt_description= models.CharField(max_length=250, null=True, default='')
    owner= models.ForeignKey('User',related_name='pins',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
