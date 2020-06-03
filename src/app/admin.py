from django.contrib import admin
from .models import *

admin.site.register({
    Description, Skills, Services, Portfolio, PortCat, Resume, Testimonials, Contact
})
