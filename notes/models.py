from django.db import models
from datetime import datetime
from users.models import User
from students.models import Student

# Create your models here.
class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Auteur')
    student = models.ManyToManyField(Student, related_name='apprenants', verbose_name='Apprenants', blank=True)
    date = models.DateTimeField(default=datetime.today, verbose_name='Date')
    subject = models.CharField(max_length=50, verbose_name='Sujet')
    note = models.TextField(max_length=3000, verbose_name='Note')
    # def __str__(self):
    #     return self.subject