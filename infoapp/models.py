from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    class_no = models.CharField(max_length=40,null=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name