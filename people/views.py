from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json

# Create your views here.

def index(request):
    entities = [{"id": i.id, "display_name": i.display_name, "twitter_id": i.twitter_id, "connects": [{"id": centity.id} for centity in i.connects.all()]} for i in Entity.objects.all()]
    return HttpResponse(json.dumps(entities), content_type="application/json")


def add(request):
    display_name = request.GET.get("display_name")
    twitter_id = request.GET.get("twitter_id")
    connects_id = request.GET.get("connects_id")
    connects_id = [] if connects_id is None else connects_id.split(",")

    try:
        entity = Entity.objects.get(twitter_id=twitter_id)
    except Entity.DoesNotExist:
        entity = Entity.objects.create(
            display_name=display_name,
            twitter_id=twitter_id
        )

    for twitter_connects_id in connects_id:
        try:
            connect_entity = Entity.objects.get(twitter_id=twitter_connects_id)
            entity.connects.add(connect_entity)
        except Entity.DoesNotExist:
            pass

    return_object = {"id": entity.id, "display_name": entity.display_name, "twitter_id": entity.twitter_id, "connects": [{"id": i.id, "display_name": i.display_name, "twitter_id": i.twitter_id} for i in entity.connects.all()]}

    return HttpResponse(json.dumps(return_object), content_type="application/json")
