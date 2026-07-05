from django.db import models

# Section B - Question 1: Define UserProfile Model with CharField, IntegerField, and BooleanField.
class UserProfile(models.Model):
    username = models.CharField(max_length=150)
    age = models.IntegerField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.username
