from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request) :
    blogs = Blog.objects.all()
    #blogs = Blog.objects.order_by('-date') [:5 ]
    return render (request,'blog/all_blog.html', {'blogs': blogs}) #Now create a templates


def detail (request, blog_id) :
    blog =  get_object_or_404 (Blog, pk=blog_id) #pk is primary key, This line tries to get the object for the particular id and if it cant, throws an error
    return render (request,'blog/detail.html', {'blog': blog})  # Now create a new template with name detail.html
