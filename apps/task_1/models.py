from django.db import models


class People(models.Model):
    name = models.CharField(max_length=255)


class Document(models.Model):
    education = models.CharField(max_length=255)
    people_id = models.ManyToManyField(People)
