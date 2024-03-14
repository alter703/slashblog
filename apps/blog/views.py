from django.shortcuts import render

app_name = 'blog'

# Create your views here.
def index(request):

    elements = {
        "elements": ['Пайтон', 'Css', 'Js', 'C++', 'C#']
    }
    return render(request, 'blog/index.html', elements)