from django.db import models

class Diver(models.Model):
    name = models.CharField(max_length=200)
    dived_at = models.DateTimeField("date published")
