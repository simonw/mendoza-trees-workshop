from django.db import models

class Species(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Tree(models.Model):
	species = models.ForeignKey(Species, on_delete=models.CASCADE)
	latitude = models.FloatField()
	longitude = models.FloatField()


