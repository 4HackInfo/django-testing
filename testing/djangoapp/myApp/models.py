from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()