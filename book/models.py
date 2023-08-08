from django.db import models

# Create your models here.


class book(models.Model):
	name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	date = models.DateField(auto_created=True,null=True,blank=True)

	def __str__(self):
		return self.name