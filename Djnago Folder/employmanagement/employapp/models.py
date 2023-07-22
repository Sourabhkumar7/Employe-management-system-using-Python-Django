from django.db import models
from django.contrib.auth.models import User
class Employe(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    
    salary=models.IntegerField()
    bonus=models.IntegerField()
    
    phone=models.IntegerField()
    hire_date=models.DateField()

class Passw(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=100)