from django.db import models

# Create your models here.
from django.forms import NumberInput


class Location(models.Model):
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.city


class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=360, default='')
    date = models.DateField(null=True, blank=True)
    time = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location")

    def __str__(self):
        return self.title


class Musician(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    instrument = models.CharField(max_length=30, default="")
    email = models.EmailField(max_length=254)
    event = models.ManyToManyField(Event, blank=True, related_name="Musician")

    def __str__(self):
        return f"{self.name} {self.surname}"


class Contact(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    cell_number = models.IntegerField(default=1)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=60)
    message = models.TextField(max_length=360, default='')
    perm = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class Comment(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    question1 = models.CharField(max_length=10)
    question5 = models.CharField(max_length=10, default="")

    options = (('1', "1"), ('2', "2"), ('3', "3"), ('4', "4"), ('5', "5"))
    question2 = models.CharField(max_length=30, choices=options, default="1")
    question3 = models.CharField(max_length=30, choices=options, default="1")
    question4 = models.CharField(max_length=30, choices=options, default="1")
    question6 = models.CharField(max_length=30, choices=options, default="1")
    question7 = models.CharField(max_length=30, choices=options, default="1")
    question8 = models.CharField(max_length=30, choices=options, default="1")
    question9 = models.TextField(max_length=360, default='')


    def __str__(self):
        return self.email


class Quizz(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    question1 = models.CharField(max_length=10)
    options = (('1', "1"), ('2', "2"), ('3', "3"), ('4', "4"), ('5', "5"))
    question2 = models.CharField(max_length=30, default="")
    question3 = models.CharField(max_length=30, choices=options, default="1")
    question4 = models.CharField(max_length=30, default="")
    question5 = models.CharField(max_length=30, default="")
    question6 = models.CharField(max_length=30, choices=options, default="1")
    question7 = models.CharField(max_length=30, default="")
    question8 = models.IntegerField()
    question9 = models.IntegerField()




    def __str__(self):
        return self.email
