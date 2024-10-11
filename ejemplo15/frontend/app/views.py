from django.shortcuts import render
import requests
import re

# Create your views here.
def index(request):
    
    context={"info": "1234"}
    return render(request, "index.html",context=context)

def about(request):
    return render(request, "about.html")