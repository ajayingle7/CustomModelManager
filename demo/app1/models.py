from django.db import models
from django.db.models import Manager
# Create your models here.



class CustomManager(Manager):
    def get_ename_startswith_A(self,ename):
        return super().get_queryset().filter(ename__startswith="A")

    def get_esal_above_1000(self,esal):
        return super().get_queryset().filter(esal__gt=1000)



class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    esal = models.FloatField()
    objects = CustomManager()


    def __str__(self):
        return f"{self.ename}--{self.esal}"


