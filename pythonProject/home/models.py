from django.db import models

# Create your models here.
class Aboutme(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='media')


    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    logo = models.CharField(max_length=300)
    def __str__(self):
        return self.name
class Feedback(models.Model):
    name = models.CharField(max_length=500)
    post = models.CharField(max_length=300)
    comment = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
class Address1(models.Model):



