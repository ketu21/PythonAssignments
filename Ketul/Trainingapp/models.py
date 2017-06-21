from django.db import models

class UserRecords(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)


