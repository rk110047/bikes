from django.db import models

# Create your models here.



class State(models.Model):
	name 		=		models.CharField(max_length=120)

	def __str__(self):
		return self.name

class City(models.Model):
	name 		=		models.CharField(max_length=120)

	def __str__(self):
		return self.name

class BikeCompany(models.Model):
	name 		=		models.CharField(max_length=120)

	def __str__(self):
		return self.name


class BikeModel(models.Model):
	name 		=		models.CharField(max_length=120)

	def __str__(self):
		return self.name
