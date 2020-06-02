from django.shortcuts import render
from .models import Description, Skills, Services, Portfolio, PortCat, Resume

# Create your views here.

def index(request):
    description = Description.objects.get(pk=1)
    skills = Skills.objects.all()
    services = Services.objects.all()
    portfolio = Portfolio.objects.all()
    p_category = PortCat.objects.all()
    resume = Resume.objects.all().order_by('-pk')

    context = {
        'description': description,
        'skills': skills,
        'services': services,
        'portfolio': portfolio,
        'p_category': p_category,
        'resume': resume
    }

    return render(request, 'index.html', context)
