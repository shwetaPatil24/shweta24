from django.db import models

# Create your models here. 
class student(models.Model):  
    age = models.IntegerField(max_length=20)  
    name = models.CharField(max_length=100)  
    roll_number = models.IntegerField(max_length=20)  
    gender = models.CharField(max_length=15)  
    class Meta:  
        db_table = "student"  