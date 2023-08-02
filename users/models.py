from django.db import models
from django import forms
from django.contrib.auth.models import User, Group


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student', related_query_name='student')
    course = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='student_course', related_query_name='student_course')
    date_of_birth = models.DateField()  # Date of birth of the student
    address = models.CharField(max_length=255)  # Address of the student
    city = models.CharField(max_length=255)  # City of the student
    country = models.CharField(max_length=255)  # Country of the student
    picture = models.ImageField(default='default.jpeg', upload_to='student_photos/')  # Student's photo
    class Meta:
        ordering =['user']
        # verbos_name ='Items'
        
    def __str__(self):
        return f'{self.user.username} Student'




