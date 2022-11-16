from django.db import models

class User(models.Model):#inherits model class  from models
 name     = models.CharField(max_length=70)
 email    = models.EmailField(max_length=100)
 password = models.CharField(max_length=100)

