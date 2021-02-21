from django.urls import path

from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='index'),
    path('about', views.about, name='about'),
    path('thanks', views.thanks, name='thanks'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('experience/', views.experience, name='experience'),
    path('contact/', views.contact, name='contact'),
    path('feed/', LatestPostsFeed(), name='post_feed')
]
