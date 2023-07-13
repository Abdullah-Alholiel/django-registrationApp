from django.db import models
from django import forms
from django.contrib.auth.models import User, Group


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    course = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='student')
    date_of_birth = models.DateField()  # Date of birth of the student
    address = models.CharField(max_length=255)  # Address of the student
    city = models.CharField(max_length=255)  # City of the student
    country = models.CharField(max_length=255)  # Country of the student
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)  # Student's photo

    def __str__(self):
        return self.user.first_name



