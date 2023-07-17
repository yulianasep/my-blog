from django.urls import path
from .views import home_view, CreatePostView, PostListView, UpdatePostView, DeletePostView, PostDetailView, AddCommentView

app_name = "blog"

urlpatterns = [
    path('', home_view, name= "home"),
    path('post/create/', CreatePostView.as_view(), name= "create_post"),
    path('post/list/', PostListView.as_view(), name= "list_post"),
    path('post/update/<int:pk>/', UpdatePostView.as_view(), name= "update_post"),
    path('post/delete/<int:pk>/', DeletePostView.as_view(), name= "delete_post"),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name= "detail_post"),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name= "add_comment"),
]