from django.db import models


class Entity(models.Model):
    id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=30)
    twitter_id = models.CharField(max_length=30)
    connects = models.ManyToManyField("self", related_name="entity_connect", blank=True)

    def __str__(self):
        return str(self.id) + " - " + self.display_name


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=30)
