from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from students.models import Student

from django.db.models.deletion import CASCADE

# Create your models here.
class Note(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    student = models.ForeignKey(Student, on_delete=CASCADE, default=0)
    date = models.DateTimeField(default=datetime.today)
    subject = models.CharField(max_length=30)
    def __str__(self):
        return self.subject