from django.db import models

class Score(models.Model): #inherits from models #representing data as class       
    name = models.CharField(max_length=50)
    value =  models.PositiveSmallIntegerField() #0-100 scores

    def __str__(self):
        return self.name # returns the name of object in Score table

    class Meta:
        ordering = ['-value']

