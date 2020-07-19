
from django.urls import path

from . import views  #because same folder me hai, so used .



app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]

#NOW go to views, and make the  function with the name all_blogs
