from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('posts/', views.posts, name='posts'),

    # CRUD
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<slug:slug>/', views.update_post, name='update_post'),
    path('delete_post/<slug:slug>/', views.delete_post, name='delete_post'),

    path('send_email/', views.sendEmail, name='send_email'),
]
