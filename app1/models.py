from django.db import models
from django.http import HttpResponse
# Create your models here.

def HomePage(request):
    return HttpResponse("<H1>Hello World</H1>")

