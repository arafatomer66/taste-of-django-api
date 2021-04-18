from django.db import models


# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, default='arafat')
    descriptions = models.TextField()
    startDate = models.CharField(null=True, max_length=200)
    endDate = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.name
