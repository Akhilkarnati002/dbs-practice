from django.db import models

class MyModel(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.username

class AccountType(models.Model):
    acc_name=models.CharField(max_length=200)



class Profile(models.Model):
    profile_id=models.OneToOneField(MyModel,on_delete=models.CASCADE)
    curr_bal=models.IntegerField()
    acc_id=models.OneToOneField(AccountType,on_delete=models.CASCADE)
