from django.shortcuts import render

from django.http import HttpResponseNotFound

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def page_not_found(request, exception):
    return render(request, 'main/page_not_found.html')