from django.db import models

class CarbonEmission(models.Model):
    date = models.DateField()
    average = models.FloatField()

    class Meta:
        ordering = ('date',)


class Pollution(models.Model):
    date = models.DateField()
    value = models.FloatField()

    class Meta:
        ordering = ('date',)
