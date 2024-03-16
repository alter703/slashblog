from django.urls import path
from . import views

app_name = 'blog' # для {% url '<app_name>:<url_name>'%}

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.detail, name='detail'),
    path('create/', views.create_post_view, name='create')
]