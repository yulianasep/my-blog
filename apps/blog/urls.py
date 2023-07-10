from django.urls import path
from .views import home_view, CreatePostView, PostListView

urlpatterns = [
    path('', home_view),
    path('post/create/', CreatePostView.as_view()),
    path('post/list/', PostListView.as_view()),
]