from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import NewURL
from django.views import View
from .forms import SubmitURLForm
from count.models import Count

# Create your views here.
class RedirectView(View):
    def get(self, request, newurl=None, *args, **kwargs):
        obj = get_object_or_404(NewURL, newurl =newurl)
        count = Count.objects.create_count(obj)
        if 'http://' not in obj.url:
            obj.url = 'http://'+obj.url
            obj.save()
        return HttpResponseRedirect(obj.url)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form  = SubmitURLForm()
        context = {
            'form': form,
            "title": 'Short Your URL'
        }
        return render(request, 'urlShorten/index.html',context)

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)

        context = {
            'form': form
        }
        template = "urlShorten/index.html"
        if form.is_valid():
            url = form.cleaned_data.get("url")
            obj, created = NewURL.objects.get_or_create(url=url)
            context = {
                "object": obj,
                "title": 'Short Your URL'
            }
            #print obj.count.count one-to-one key
            if created:
                template = "urlShorten/created.html"
            else:
                template = "urlShorten/existed.html"
        return render(request, template, context)