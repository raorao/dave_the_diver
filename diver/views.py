from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from diver.models import Diver

def index(request):


    names = [d.name for d in Diver.objects.all()]
    return HttpResponse("Dave the diver!! with names: " + ", ".join(names))