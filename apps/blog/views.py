from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from apps.blog import models

# Create your views here.

def home_view(request):
    return render(request,"home.html")

class PostListView(ListView):
    template_name = "PostListView.html"
    model = models.Post
    context_object_name = 'post_list'

class CreatePostView(CreateView):
    template_name = "CreatePostView.html"
    fields = '__all__'
    model = models.Post
    success_url = ''
