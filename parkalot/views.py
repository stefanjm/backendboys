from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    # Render the template
    return render(request, 'parkalot/index.html')