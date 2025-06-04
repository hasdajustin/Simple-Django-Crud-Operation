from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_data, name='display_data'),
    path('add_newUser/', views.add_newUser, name='add_newUser'),
    path('edit_userinfo/<int:pk>/', views.edit_userinfo, name='edit_userinfo'),
    path('delete_userinfo/<int:pk>/', views.delete_userinfo, name='delete_userinfo'),
]
