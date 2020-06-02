from django.shortcuts import render
from .models import Description, Skills, Services, Portfolio, PortCat, Resume

import requests

def medium_request():
    url_medium = 'https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@eduar766'
    response = requests.get(url_medium).json()
    data = []
    response = response['items']
    length = len(response)
    p = 0

    while p < length:
        collect = {
            'title': response[p]['title'],
            'link': response[p]['link'],
            'pub_date': response[p]['pubDate'],
            'description': response[p]['description'],
            'thumbnail': response[p]['thumbnail'],
        }

        data.append(collect)
        p = p + 1 

    print(data)

    return data

def index(request):
    description = Description.objects.get(pk=1)
    skills = Skills.objects.all()
    services = Services.objects.all()
    portfolio = Portfolio.objects.all()
    p_category = PortCat.objects.all()
    resume = Resume.objects.all().order_by('-pk')

    medium = medium_request()

    context = {
        'description': description,
        'skills': skills,
        'services': services,
        'portfolio': portfolio,
        'p_category': p_category,
        'resume': resume,
        'medium': medium
    }

    return render(request, 'index.html', context)
