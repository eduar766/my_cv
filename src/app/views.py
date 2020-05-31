from django.shortcuts import render
from .models import Description, Skills, Services

# Create your views here.

def index(request):
    description = Description.objects.get(pk=1)
    skills = Skills.objects.all()
    services = Services.objects.all()

    context = {
        'description': description,
        'skills': skills,
        'services': services
    }

    return render(request, 'index.html', context)
