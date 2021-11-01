from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json

# Create your views here.

def index(request):
    entities = [{"id": i.id, "display_name": i.display_name, "twitter_id": i.twitter_id, "connects": i.connects} for i in Entity.objects.all()]
    return HttpResponse(json.dumps(entities), content_type="application/json")
