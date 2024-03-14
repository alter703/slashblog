from django.shortcuts import render

from .models import Post


app_name = 'blog'

# Create your views here.
def index(request, id):

    elements = {
        "elements": ({'id': 1, 'text':'Python'}, {'id': 2, 'text':'C#'}, {'id': 3, 'text':'C++'}, {'id': 4, 'text':'Java'})
    }

    print(id)
    return render(request, 'blog/index.html', elements)