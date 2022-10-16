
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phonenumber = models.BigIntegerField(default=None)
    aadhar_card = models.CharField(max_length=20,default=None,null=True)
    pan_card = models.CharField(max_length=20,default=None,null=True)
    dob = models.DateField()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['phonenumber','aadhar_card','pan_card','dob']

    def __str__(self):
        return self.username


class AccountType(models.Model):
    Name= models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.Name

class Profile(models.Model):
    current_balance =  models.IntegerField(default=1000)
    account_type_id = models.ForeignKey(AccountType,on_delete= models.CASCADE,default=3)
    user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)


