from django.db import models

# Create your models here.
class Marks(models.Model):
    m1=models.CharField(max_length=5,null=False)
    m2=models.CharField(max_length=5,null=False)
    m3=models.CharField(max_length=5,null=False)
    name=models.CharField(max_length=150,null=False)
    total=models.CharField(max_length=10,null=True)
    
    
    def __str__(self):
        return f"{self.m1},{self.m2},{self.m3},{self.name},{self.total}"