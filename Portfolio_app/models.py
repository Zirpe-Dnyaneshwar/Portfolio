from django.db import models

# Create your models here.
class contact_data(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    msg=models.CharField(max_length=500)