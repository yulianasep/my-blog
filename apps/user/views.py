from django.shortcuts import render, HttpResponse, get_object_or_404
from apps.user.form import UserForm
from apps.user.models import User

# Create your views here.
def home_view(request):
    return render(request,"home.html")

def create_user(request):
    if request.method == 'GET':
        context = {
            'form': UserForm
        }
        return render(request, 'createUser.html', context)
    
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
        else:
            context = {
                'form': form
            }
            return render(request, 'createUser.html', context)

def update_user(request, pk=None):
    if request.method == 'GET':
        user = User.objects.filter(pk=pk)

        if user.exists():
            user = user.first()
            form = UserForm(instance=user)
            context = {
                'form': form
            }
            return render(request, 'updateUser.html', context)
        else:
            return HttpResponse("404")
    
    elif request.method == 'POST':
        user = User.objects.filter(pk=pk)

        if user.exists():
            user = user.first()
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return render(request, 'user:home.html')
            else:
                context = {
                    'form': form
                }
                return render(request, 'updateUser.html', context)
        else:
            return HttpResponse("404")
        

def delete_user(request, pk=None):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return render(request, 'listUser.html')

    
def list_user(request):
    if request.method == 'GET':
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, 'listUser.html', context)
    