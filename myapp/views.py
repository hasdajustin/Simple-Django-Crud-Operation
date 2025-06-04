from django.shortcuts import render

# Create your views here.
def display_data(request):
    return render(request, 'myapp/display_data.html')
