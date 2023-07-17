from django.urls import path
from .views import home_view, create_user, update_user, delete_user, list_user

app_name = "user"

urlpatterns = [
    path('', home_view, name= "home"),
    path('create/', create_user, name= "create"),
    path('update/<int:pk>/', update_user, name= "update"),
    path('delete/<int:pk>/', delete_user, name= "delete"),
    path('list/', list_user, name= "list"),
]