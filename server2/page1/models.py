# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length = 200)
    salary = models.IntegerField(default = 500)
