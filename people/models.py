from django.db import models


class Entity(models.Model):
    id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=30)
    twitter_id = models.CharField(max_length=30)
    connects = models.ManyToManyField("self", related_name="entity_connect", blank=True)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=30)
