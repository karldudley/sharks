from django.db import models

# Create your models here.

class Species(models.Model):
    name = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    adorable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Shark(models.Model):
    name = models.CharField(max_length=100)
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name
