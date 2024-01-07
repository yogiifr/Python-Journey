from django.db import models

# Create your models here.
class Member(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.firstName + ' ' + self.lastName