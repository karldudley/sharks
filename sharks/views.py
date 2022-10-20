from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Shark

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return HttpResponse("<h1>About</h1>")

def list(request):
    sharks = Shark.objects.all()
    return render(request, "shark-list.html", { "sharks": sharks})

def show(request, id):
    shark = get_object_or_404(Shark, pk=id)
    # return HttpResponse(f"<h1>Hey, {shark.name}</h1>")
    return render(request, 'shark-show.html', { "shark": shark})
