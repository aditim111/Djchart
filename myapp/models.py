from django.db import models

# Create your models here.


class Population(models.Model):
	population  = models.CharField(max_length=50, null=True,blank=True)
	growth_rate = models.CharField(max_length=50)
	year = models.CharField(max_length=50)
	