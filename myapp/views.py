from django.shortcuts import render, redirect
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



