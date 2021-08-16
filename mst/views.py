from django.shortcuts import render
from .getData import get
from .models import post
from django.http import HttpResponse, HttpRequest, request
# Create your views here.

def index(request):
    return render(request, 'index.html')

def Search(request:HttpRequest):
    taxCode = post(TAXCODE = request.POST['TAXCODE'])
    totalCode = post.objects.all()
    for i in totalCode:
        if taxCode.TAXCODE == i.TAXCODE:
            context = {'lists': get(taxCode.TAXCODE)}
            return render(request, 'index.html', context)
                    
    taxCode.save()
    Context = {'lists' : get(taxCode.TAXCODE)}
    
    return render(request, 'index.html', Context)