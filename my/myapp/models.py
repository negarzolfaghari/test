from django.db import models

# Create your models here.
class Phone(models.Model):
    name=models.CharField(max_length=100)
    family=models.CharField(max_length=100)
    phone=models.CharField(max_length=11)
    MALE="مرد"
    FEMALE="زن"
    GENDER_TYPE=((MALE,MALE),(FEMALE,FEMALE))
    gender=models.CharField(max_length=7,choices=GENDER_TYPE)
    def __str__(self) :
        return f"{self.name}{self.family}{self.phone}{self.gender}"