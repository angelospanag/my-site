from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='index'),
    path('about', views.about, name='about'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact, name='contact')
]
