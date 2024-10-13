from django.db import models

# Create your models here.
class Student(models.Model):
    no=models.IntegerField(null=True)
    name=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=10,null=True)
    hobbies=models.TextField(null=True)
    course=models.CharField(max_length=100,null=True)
    
    
    
    def __str__(self):
        return f"{self.name},{self.no},{self.gender},{self.hobbies},{self.course}"

