from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'

class AboutView(generic.TemplateView): #it does not need a model because it's static page, not taking anything from database
    template_name = 'about.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created') #only published posts ordered by date
    template_name = 'index.html'
    