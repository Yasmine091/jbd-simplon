from django.db import models
from datetime import datetime
from users.models import User
from students.models import Student

# Create your models here.
class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.today)
    subject = models.CharField(max_length=50)
    note = models.TextField(max_length=3000)