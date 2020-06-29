from django.urls import path
from django.contrib import admin
from . import views 

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('files/', views.files_list, name='files_list'),
    path('files/upload/', views.upload_files, name='upload_files'),
    path('files/encrypt/', views.encrypt_files, name='encrypt_files'),
    path('files/decrypt/', views.decrypt_files, name='decrypt_files')
]