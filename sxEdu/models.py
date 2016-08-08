from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

class Student(models.Model):
	studentId = models.CharField(max_length=64)
	studentName = models.CharField(max_length=64)
	createDate = models.DateTimeField(auto_now_add=True)
	comments = models.TextField(null=True,blank=True)

class Opus(models.Model):
    studentId = models.CharField(max_length=64)
    imageTitle = models.CharField(max_length=64,blank=True,null=True)
    opusImage = models.ImageField(upload_to='upload')
    createDate = models.DateTimeField(auto_now_add=True)    

admin.site.register(Student)
admin.site.register(Opus)

