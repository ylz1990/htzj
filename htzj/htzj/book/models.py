from django.db import models
from tinymce.models import HTMLField
# Create your models here.

# CREATE DATABASE mydb1 CHARACTER SET utf8 COLLATE utf8_general_ci;

class User(models.Model):
    name = models.CharField(max_length=20)
    passwords = models.CharField(max_length=10)

class Bookinfo(models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=50,default="")
    pub_time = models.DateTimeField()
    new_type = models.CharField(max_length=10,default="")
    content = HTMLField()


    # user = models.ForeignKey("User",on_delete=models.CASCADE,default='')

# class Newinfo(models.Model):
#     # id = models.AutoField(primary_key=True)
#     author = models.CharField(max_length=10)
#     title = models.CharField(max_length=50,default="")
#     pub_time = models.DateTimeField()
#     new_type = models.CharField(max_length=10)
#     content = HTMLField()
#
# class Goldinfo(models.Model):
#     # id = models.AutoField(primary_key=True)
#     author = models.CharField(max_length=10)
#     title = models.CharField(max_length=50,default="")
#     pub_time = models.DateTimeField()
#     new_type = models.CharField(max_length=10)
#     content = HTMLField()