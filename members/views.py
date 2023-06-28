from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#def members(request):
    #return HttpResponse("Hello world!")
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render())
    #template = loader.get_template('shopitem.html')
    #return HttpResponse(template.render())

    #
    #def indexpage(request):
  #context = {'selected_page': 'index'}
 # return render(request, 'index.html', context)

 # def shopitempage(request):
 # context = {'selected_page': 'shopitem'}
 # return render(request, 'shopitem.html', context)

from django.shortcuts import render

def members(request):
    return render(request, 'index.html',)

def indexpage(request):
    context = {'selected_page': 'index'}
    return render(request, 'index.html', context)

def shopitempage(request):
    context = {'selected_page': 'shopitem'}
    return render(request, 'shopitem.html', context)
#
