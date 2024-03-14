from django.shortcuts import render

app_name = 'blog'

# Create your views here.
def index(request):

    elements = {
        "elements": ({'id': 1, 'text':'Python'}, {'id': 2, 'text':'C#'}, {'id': 3, 'text':'C++'}, {'id': 4, 'text':'Java'})
    }
    # elements = {
    #     'elements': ({'id': 1, 'text':'Hello'}, {'id': 2, 'text':'Hello'}, {'id': 3, 'text':'Hello'}, {'id': 4, 'text':'Hello'})
    # }
    return render(request, 'blog/index.html', elements)