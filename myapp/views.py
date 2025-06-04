from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

# Create your views here.
def display_data(request):
    userData = User.objects.all()
    return render(request, 'myapp/display_data.html', {'userData':userData})

# model form use kore data add korar jonno
def add_newUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_data') # kheyal rakhte hobe ekhane kono ".html" use hobe na just "display_data" function er name er nam hobe.
    else:
        form = UserForm()
    return render(request,'myapp/add_newUser.html', {'form':form})

def edit_userinfo(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('display_data')
    else:
        form = UserForm(instance=user) # user er sob data gula form e show korbe.
    return render(request, 'myapp/edit_userinfo.html', {'form': form})

def delete_userinfo(requeset, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('display_data')