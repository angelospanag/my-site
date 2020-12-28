from django.urls import path

from .views import contact, home

app_name = 'blog'

urlpatterns = [
    path('', home),
    path('contact/', contact)
]
