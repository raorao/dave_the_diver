from django.db import models

class Diver(models.Model):
    name = models.CharField(max_length=200)
    dived_at = models.DateTimeField("date published")

    def __str__(self):
        return f'Diver: {self.name}'
