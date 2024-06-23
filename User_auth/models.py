from django.db import models

# Create your models here.

from datetime import datetime;
from django.contrib.auth.models import User

now = datetime.now()
time_sting = now.strftime("%H:%M:%S")
dt_sting = now.strftime("%Y-%m-%d")

class newuser(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    

# myapp/models.py



class Document(models.Model):
    FILE_TYPES = [
        ('pdf', 'PDF'),
        ('xls', 'Excel'),
        ('doc', 'Word'),
        ('docx', 'Word'),
    ]
    
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=4, choices=FILE_TYPES)

    def __str__(self):
        return self.file.name
