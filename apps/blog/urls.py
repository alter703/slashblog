from django.urls import path
from . import views

app_name = 'blog' # для {% url 'blog:<name>'%}

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>', views.detail, name='detail'),
    path('create/', views.create_view, name='create')
]