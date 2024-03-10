from django.db import models

# Create your models here.
class roomdetails(models.Model):
    no_of_rooms=models.TextField(max_length=255)
    type_of_room=models.TextField(max_length=255)
    no_of_people=[
        ('adults','Adults'),
        ('children','Children'),
    ]
    noofpeople=models.CharField(max_length=20, choices=no_of_people)

def __str__(self):
    return self.no_of_rooms

