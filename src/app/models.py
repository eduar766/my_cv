from django.db import models

# Create your models here.

class Description(models.Model):
    text = models.TextField()
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.text


class Skills(models.Model):
    title = models.CharField(max_length=30)
    progress = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    

class Services(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title


class PortCat(models.Model):
    cat = models.CharField(max_length=50)
    
    def __str__(self):
        return self.cat
    

class Portfolio(models.Model):
    
    project = models.CharField(max_length=80)
    category = models.ManyToManyField(PortCat)
    description = models.TextField()
    image = models.ImageField()
    url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.project
    

class Resume(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    fecha_inicio = models.CharField(max_length=20)
    fecha_final = models.CharField(max_length=20)
    icon = models.CharField(max_length=20)
    job = models.CharField(max_length=50, blank=True, null=True)
    technologies = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
    

class Testimonials(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField()
    job = models.CharField(max_length=50)
    testimonial = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    address = models.CharField(max_length=120)
    cellphone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email