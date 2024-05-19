from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Grade(models.Model):
    grade_name = models.CharField(max_length=100)

    def __str__(self):
        return self.grade_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="student_info")
    phone_number = models.CharField(max_length=10,null=True)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE,related_name="students",null=True)
    subject = models.ManyToManyField(Subject,related_name="student_subjects")
    
    def __str__(self):
        return f"{self.student}"

class Mark(models.Model):
    assessment = models.CharField(max_length=30,null=True)
    percentage = models.IntegerField()
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="subject_mark")
    student = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="student_mark")

class Announcement(models.Model):
    content = models.CharField(max_length=432)
    poster = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="poster_announcement")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Announcement by {self.poster} on {self.date.strftime('%d %b %Y %H:%M:%S')}" 