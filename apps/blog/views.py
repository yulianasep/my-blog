from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView

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
    context_object_name = 'post_list'

class CreatePostView(CreateView):
    template_name = "CreatePostView.html"
    fields = '__all__'
    model = models.Post
    success_url = 'list_post'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('home')

class UpdatePostView(UpdateView):
    template_name = "UpdatePostView.html"
    fields = '__all__'
    model = models.Post
    success_url = 'list_post'


class DeletePostView(DeleteView):
    template_name = "DeletePostView.html"
    model = models.Post
    success_url = 'list_post'

class AddCommentView(CreateView):
    template_name = "AddCommentView.html"
    fields = '__all__'
    model = models.Comment
    success_url = 'list_post'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('home')