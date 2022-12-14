from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect

# Create your views here.

def scrape(request):
    if request.method =="POST":
        site = request.POST.get('site', '')

    #Pass site to page:
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
    

        for link in soup.find_all('a'):
            link_address = (link.get('href'))
            link_text = link.string
            #create object based on Model, passing variables as parameters:
            Link.objects.create(address = link_address, name = link_text)
        return HttpResponseRedirect('/')

    else:
        #extract data from database:
        data = Link.objects.all()

    return render(request, 'myapp/result.html', {"data":data})

def clear(request):
    Link.objects.all().delete() #delete alll objects
    return render(request, 'myapp/result.html')