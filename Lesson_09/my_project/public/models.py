from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=100)
	birthdate = models.DateField(blank=True, null=True)

	def __str__(self):
		return 'Author: ' + self.name


class Book(models.Model):
	title = models.CharField(max_length=100)
	isbn = models.CharField(max_length=100, unique=True)
	authors = models.ManyToManyField(to=Author)
	slug = models.SlugField()

class CharField:
	def __get__(self, obj, name):
		pass

	def __set__(self, name, value):
		pass




		