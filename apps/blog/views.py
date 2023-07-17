from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, 
                                  ListView, 
                                  UpdateView, 
                                  DeleteView, 
                                  DetailView)

from apps.blog import models

# Create your views here.

def home_view(request):
    return render(request,"home.html")

class PostDetailView(DetailView):
    template_name = "PostDetailView.html"
    model = models.Post
    context_object_name = 'post'
    
class PostListView(ListView):
    template_name = "PostListView.html"
    model = models.Post
    context_object_name = 'list_post'
class CreatePostView(CreateView):
    template_name = "CreatePostView.html"
    fields = '__all__'
    model = models.Post
    success_url = reverse_lazy('blog:list_post')


def update_post(request, pk=None):
    if request.method == 'GET':

        post = models.Post.objects.filter(pk=pk)
        
        if post.exists():
            post = post.first()
            context = {
                'post': post
            }
            return render(request, 'UpdatePostView.html', context)


class UpdatePostView(UpdateView):
    template_name = "UpdatePostView.html"
    fields = '__all__'
    model = models.Post
    success_url = reverse_lazy('blog:list_post')

class DeletePostView(DeleteView):
    template_name = "PostDeleteView.html"
    model = models.Post
    success_url = reverse_lazy('blog:list_post')

class AddCommentView(CreateView):
    template_name = "AddCommentView.html"
    fields = '__all__'
    model = models.Comment
    success_url = reverse_lazy('blog:list_post')