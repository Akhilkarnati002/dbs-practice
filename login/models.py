from django.db import models

class MyModel(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=50,null=True)
    cpassword=models.CharField(max_length=50,null=True)