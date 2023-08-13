from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
