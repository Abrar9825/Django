from django.db import models


# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=100,null=False)
    email=models.CharField(max_length=100,null=False)
    password=models.CharField(max_length=100,null=False)
    gender=models.CharField(max_length=100,null=False)
    choice=models.CharField(max_length=100,null=False)
    interests=models.TextField(max_length=100,null=False)
    
    
    def __str__(self):
        return f"{self.name},{self.email},{self.password},{self.gender},{self.choice},{self.interests}"