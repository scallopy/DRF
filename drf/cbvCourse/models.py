from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    ratings = models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***')])

    def __str__(self):
        return self.id+self.name+self.description+self.ratings
