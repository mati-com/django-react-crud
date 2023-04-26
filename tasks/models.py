from django.db import models

# Create your models here.

class Task(models.Model):
    tittle = models.CharField(max_length = 250)
    description = models.TimeField(blank = True)
    done = models.BooleanField(default = False)
