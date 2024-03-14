from django.urls import path
from . import views

app_name = 'blog' # для {% url 'blog:<name>'%}

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.index, name='index'),
]