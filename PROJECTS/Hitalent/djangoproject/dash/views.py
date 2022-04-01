from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to HITALENT!</h1>')

def dashboard(request):
    return HttpResponse('<h1>Welcome User!</h1>')