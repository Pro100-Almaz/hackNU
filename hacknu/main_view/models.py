from django.db import models

class PersonCardinates(models.Model):
    x_card = models.IntegerField()
    y_card = models.IntegerField()
    z_card = models.IntegerField()
    timestamps = models.IntegerField()
