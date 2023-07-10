from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

# Create your views here.

def home_view(request):
    print("Hola")
    return render(request,"home.html")


class Post(TemplateView):
    template_name = "post.html"




