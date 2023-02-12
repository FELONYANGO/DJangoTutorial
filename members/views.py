from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

# Create your views here.
def  members(request):
    template=loader.get_template('base.html')
    member=Members.objects.all().values()
    context={
        'member':member
    }
    return HttpResponse(template.render(context,request))
    