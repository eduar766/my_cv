from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

import requests
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailForm

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

    return data

global message
global name
global email

def email_(name, email, message):
    subject = '{name} Gracias por escribirme'.format(name=name)
    message = 'Hola, es Eduardo Saavedra. Muchas gracias por escribirme, Significa mucho para mi. En cuanto tenga la posibilidad te devolvere el correo.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['eduar766@gmail.com', email]
    send_mail( subject, message, email_from, recipient_list )

    return redirect('index')



def index(request):
    description = Description.objects.get(pk=1)
    skills = Skills.objects.all()
    services = Services.objects.all()
    portfolio = Portfolio.objects.all()
    p_category = PortCat.objects.all()
    resume = Resume.objects.all().order_by('-pk')
    testimonials = Testimonials.objects.all()
    contact = Contact.objects.get(pk=1)

    
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():  
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            qq = form.save() 
    
        send_e = email_(name, email, message)


    medium = medium_request()

    context = {
        'description': description,
        'skills': skills,
        'services': services,
        'portfolio': portfolio,
        'p_category': p_category,
        'resume': resume,
        'medium': medium,
        'testimonials': testimonials,
        'contact': contact
    }

    return render(request, 'index.html', context)


