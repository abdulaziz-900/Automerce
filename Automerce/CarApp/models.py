from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cars(models.Model):
    Model=models.CharField(max_length=64)
    price=models.IntegerField()
    type=models.CharField(max_length=64)
    Cname=models.CharField(max_length=64)
    ModelYear=models.IntegerField()
    colour=models.CharField(max_length=64,null=True)
    engineType=models.CharField(max_length=64,null=True)
    customer=models.ManyToManyField(User,null=True,blank=True ,related_name="cars")#,on_delete=models.CASCADE
    




    


