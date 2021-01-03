from django.db import models

# Create your models here.
class Passenger(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    travelPoints = models.CharField(max_length=100)

    def __str__(self):
        return self.id+self.firstName+self.lastName+self.travelPoints
