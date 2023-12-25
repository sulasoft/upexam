from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True)
    favorite_profiles = models.ManyToManyField('Profile', related_name='favorited_by', blank=True)

    def save(self, *args, **kwargs):
        if self.email and (not self.username or self.username != self.email):
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.email)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}'s Profile"

class FavoriteProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favorite_profiles')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email}'s Favorite Profile"