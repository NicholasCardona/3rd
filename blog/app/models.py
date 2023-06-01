from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)




    def __str__(self):
        return self.title 
    



class Student(models.Model):
    name = models.TextField()
    VeryPoor = 'Very Poor'
    Poor = 'Poor'
    Mid = 'Normal'
    Rich = 'Rich'
    VeryRich = 'Very Rich'
    CHOICES = [
        (Poor, "Poor"),
        (VeryPoor, "Very Poor"),
        (Mid, "Mid"),
        (Rich, " Rich"),
        (VeryRich, "Very Rich")]
    
    Finances = models.CharField(
        max_length=9,
        choices=CHOICES,
        default='mid',
    )
    
    body = models.TextField()
    
    def __str__(self):
        return self.name
    
    def shorten(self):
        return self.body[:50] + '...'
    


class Drivers(models.Model):
    TEAMS = (
    ('RedBull' , 'Redbull'),
    ('Mercedes' , 'Mercedes'),
    ('AstonMartin' , 'Aston Martin'),
    ('Ferrari', 'Ferrari'),
    ('AlphaTauri', 'Alpha Tauri'),
    ('AlphaRomeo', 'Alpha Romeo'),
    ('Williams', 'Williams'),
    ('Hass', 'Hass'),
    ('McLaren', 'McLaren'),
    ('Alpine', 'Alpine'),
    )
    
    name = models.TextField()
    team = models.CharField(max_length=20, choices=TEAMS)
    thumb = models.ImageField(default='default_f1.jpeg', blank=True)


    def __str__(self):
        return self.name


