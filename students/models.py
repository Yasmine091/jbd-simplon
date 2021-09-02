from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    classe = models.CharField(max_length=8)
    def __str__(self):
        return str(self.firstname) + ' ' + str(self.lastname)