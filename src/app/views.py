from django.shortcuts import render
from .models import Description, Skills, Services, Portfolio, PortCat

# Create your views here.

def index(request):
    description = Description.objects.get(pk=1)
    skills = Skills.objects.all()
    services = Services.objects.all()
    portfolio = Portfolio.objects.all()
    p_category = PortCat.objects.all()

    context = {
        'description': description,
        'skills': skills,
        'services': services,
        'portfolio': portfolio,
        'p_category': p_category
    }

    return render(request, 'index.html', context)
