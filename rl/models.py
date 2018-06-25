from __future__ import unicode_literals

from django.db import models

import datetime

year_dropdown = []
for y in range(1900, (datetime.datetime.now().year)):
    year_dropdown.append((y, y))

class Loc(models.Model):
	name = models.CharField(max_length=75, blank=False)
	lon = models.CharField(max_length=75, blank=False)
	lat = models.CharField(max_length=75, blank=False)
	date = models.IntegerField(('year'),  choices=year_dropdown, default=datetime.datetime.now().year)
	link=models.CharField(max_length=75,blank=False)
	status=models.CharField(max_length=75,blank=False,default="false")


class adder(models.Model):
	fname = models.CharField(max_length=75, blank=False)
	sname = models.CharField(max_length=75, blank=False)
	email= models.EmailField(max_length=75, blank=False)
	pswd = models.CharField(max_length=75, blank=False)

