import random, string
from django.conf import  settings
SHORTURL_MIN = getattr(settings, "SHORTURL_MIN", 6)

def random_url(size=SHORTURL_MIN, chars = string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_url(instance, size= SHORTURL_MIN):
    newurl = random_url(size=size)
    NewURL = instance.__class__
    queryset_exist = NewURL.objects.filter(newurl = newurl).exists()
    if queryset_exist:
        return create_url(size=size)
    return newurl