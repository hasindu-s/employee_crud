import email
from pyexpat import model
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return self.name