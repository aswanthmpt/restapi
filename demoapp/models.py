from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=222)
    age=models.IntegerField()
    place=models.TextField()
    def __str__(self):
        return self.name