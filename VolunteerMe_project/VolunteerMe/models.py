from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    TYPE_CHOICES = (('v', 'volunteer'), ('o', 'organiser'))
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    name = models.CharField(max_length=128, help_text='Full Name')
    email = models.EmailField(help_text='Email')
    contact_number = models.CharField(max_length=15, help_text='Contact number')
    post_code = models.CharField(max_length=12, blank=True, help_text='postcode')
    address = models.CharField(max_length=128, blank=True, help_text='address')
    town = models.CharField(max_length=128, blank=True, help_text='Town')
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class EditUserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    name = models.CharField(max_length=128, help_text='Full Name')
    email = models.EmailField(help_text='Email')
    contact_number = models.CharField(max_length=15, help_text='Contact number')
    post_code = models.CharField(max_length=12, blank=True, help_text='postcode')
    address = models.CharField(max_length=128, blank=True, help_text='address')
    town = models.CharField(max_length=128, blank=True, help_text='Town')
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Opportunity(models.Model):
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128, default='other')
    company = models.ForeignKey(UserProfile, default=None)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    # Should not be able to make this blank.
    # Instead, an empty string signifies NULL
    description = models.TextField(blank=False, default='')
    location = models.TextField(blank=True, default="")
    optional = models.TextField(blank=True, default="None")

    def __unicode__(self):
        return self.name


class Application(models.Model):
    volunteer = models.ForeignKey(User)
    opportunity = models.ForeignKey(Opportunity)


class Reply(models.Model):
    answer = models.BooleanField(blank=True, default=None)
    application = models.ForeignKey(Application)

    class Meta:
        verbose_name_plural = 'Replies'


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'