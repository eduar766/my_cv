from django.db import models

# Create your models here.

class Description(models.Model):
    text = models.TextField()

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
    