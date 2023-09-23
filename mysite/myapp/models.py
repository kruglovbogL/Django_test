from django.db import models

class Leaning(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    duration = models.IntegerField(default=5)

    def __str__(self):
        return (self.name, self.link, self.duration)

class Product(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    acsess = models.CharField(max_length=50)
   # name_leaning = models.ForeignKey(Leaning, on_delete=models.CASCADE)


    def __str__(self):
        return (self.name, self.owner, self.acsess)

class User(models.Model):
    name = models.CharField(max_length=50)
    values = models.IntegerField()

    def __str__(self):
        return (self.name, self.values)