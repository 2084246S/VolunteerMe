from django.db import models


class Volunteer(models.model):
    firstname = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    email = models.EmailField()
    gender = models.ChoiceField(blank=True)
    time_available = models.ChoiceField(blank=True)
    contact_number = models.IntegerField(max_length=15,blank=True)

    def __unicode__(self):
        return self.name


class Search(models.Model):
    town_or_postcode = models.CharField(blank=True)
    distance_from = models.IntegerField(blank=True)
    category = models.ChoiceField(blank=True)
    optional = models.ChoiceField(blank=True)

    def __unicode__(self):
        return self.name


class Organiser(models.Model):
    company_name = models.CharField()
    company_email = models.EmailField()
    company_number = models.IntegerField()
    company_address = models.CharField()

    def __unicode__(self):
        return self.name


class Opportunities(models.Model):
    category = models.ChoiceField()
    time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    optional = models.TextField(blank=True)

    def __unicode__(self):
        return self.name