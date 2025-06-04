from django.shortcuts import render
from .models import User

# Create your views here.
def display_data(request):
    userData = User.objects.all()
    return render(request, 'myapp/display_data.html', {'userData':userData})
