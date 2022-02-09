from django.db import models

class Event(models.Model):

    event =                models.CharField(max_length=50)
    capacity =             models.PositiveIntegerField()
    event_hall =           models.CharField(max_length=30)
    hall_address =         models.CharField(max_length=50)
                  
class User(models.Model):

    email      =           models.EmailField()
    username   =           models.CharField(max_length=20)
    first_name =           models.CharField(max_length=20)
    last_name  =           models.CharField(max_length=20)