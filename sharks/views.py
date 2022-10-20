from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Shark

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def list(request):
    sharks = Shark.objects.all()
    return render(request, "shark-list.html", { "sharks": sharks})

@login_required
def show(request, id):
    shark = get_object_or_404(Shark, pk=id)
    return render(request, 'shark-show.html', { "shark": shark})
