from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')), # HTML Views
    path('api/', include('myapp.api_urls')) # API View
]
