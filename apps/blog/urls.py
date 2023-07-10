from django.urls import path
from .views import home_view, Post

urlpatterns = [
    path('/', home_view),
    path('/post', Post.as_view()),
]