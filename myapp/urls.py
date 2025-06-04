from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_data, name='display_data'),
    path('add_newUser/', views.add_newUser, name='add_newUser'),
]
