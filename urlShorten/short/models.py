from __future__ import unicode_literals
from django.db import models
from utils import random_url, create_url
from django.conf import settings
from .validators import URLValidator
from django_hosts.resolvers import reverse

SHORTURL_MAX = getattr(settings, "SHORTURL_MAX", 15)

class NewURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(NewURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active= True)
        return qs

    def refresh_url(self, items = None):
        queryset = NewURL.objects.filter(id_gte=1)
        if items and isinstance(items, int):
            queryset = queryset.order_by('-id')[:items]
        for q in queryset:
            q.newurl = create_url(q, )
            q.save()


# Create your models here.
class NewURL(models.Model):
    url = models.CharField(max_length=200, validators=[URLValidator,])
    newurl = models.CharField(max_length=SHORTURL_MAX, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = NewURLManager()

    def save(self, *args, **kwargs):
        if not self.newurl or self.newurl=='':
            self.newurl = create_url(self)
        super(NewURL, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.url)

    def get_new_url(self):
        return reverse('created_url',kwargs={'newurl':self.newurl}, host='www',scheme='http',port='5000')

