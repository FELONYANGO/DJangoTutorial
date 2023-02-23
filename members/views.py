from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

# Create your views here.
def  members(request):
    template=loader.get_template('base.html')
    myMembers=Members.objects.all().values()
    context={
        'myMembers':myMembers
    }
    return HttpResponse(template.render(context,request))
    
def details(request,slug):
    myMembers=Members.objects.get(slug=slug)
    template=loader.get_template('details.html')
    context={
        'myMembers':myMembers,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())


def tests(request):
   
    template=loader.get_template('tests.html')
    context={
       
     'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context,request))