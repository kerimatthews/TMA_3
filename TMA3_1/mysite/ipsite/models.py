from django.db import models


class My_model(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  ip = models.GenericIPAddressField()
  num_visits = models.IntegerField()