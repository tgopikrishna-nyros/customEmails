# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Nform(models.Model):
	to = models.CharField(max_length=100)
	subject = models.CharField(max_length=200)
	body = models.TextField()
	def __str__(self):
		return self.to

class Trashmail(models.Model):
	remove_id = models.IntegerField()
	mail = models.CharField(max_length=100)
	subject = models.CharField(max_length=200)
	body = models.TextField()
	def __str__(self):
		return self.mail

