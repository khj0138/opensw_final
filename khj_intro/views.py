

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

#from .models import Candidate

def home(request):
    #candidates = Candidate.objects.all()
    return render(request, 'elections/home.html')

def interest(request):
    return render(request, 'elections/interest.html')

def basic(request):
    return render(request, 'elections/basic.html')

def mbti(request):
    return render(request, 'elections/mbti.html')
