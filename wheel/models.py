from django.db import models
from django.contrib.auth.models import User

class Wheel(models.Model):
    name = models.CharField(max_length = 200)
    owner = models.ForeignKey(User)
    sectors_number = models.IntegerField()
    max_value = models.IntegerField()
    step_value = models.IntegerField()

    def __str__(self):
        return self.name

class Sector(models.Model):
    wheel = models.ForeignKey('Wheel', related_name="sectors", related_query_name="sector")
    name = models.CharField(max_length = 200)
    value = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
