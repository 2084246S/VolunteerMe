from django.db import models
from django.utils.text import slugify

class Volunteer(models.Model):
    firstname = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    email = models.EmailField()
    gender = models.CharField(max_length=32, choices=((1, "Male"), (2, "Female"), (3, "Other")))
    time_available = models.DateField()
    contact_number = models.CharField(max_length=15, blank=True)

    def __unicode__(self):
        return self.name


class Search(models.Model):
    town_or_postcode = models.CharField(max_length=128, blank=True)
    distance_from = models.IntegerField(blank=True)
    category = models.CharField(max_length=128)
    optional = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Organiser(models.Model):
    company_name = models.CharField(max_length=128)
    company_email = models.EmailField()
    company_number = models.IntegerField()
    company_address = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Opportunity(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.CharField(max_length=128, default="Other")
    #time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    location = models.TextField(blank=True, default="")
    optional = models.TextField(blank=True, default="")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self.name))
        super(Opportunity, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Category(models.Model):

    job_name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name