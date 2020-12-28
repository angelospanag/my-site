from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact)
]
