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