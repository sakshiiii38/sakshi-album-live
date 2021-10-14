from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('gallery/', views.gallery , name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto , name='photo'),
    path('add/', views.addPhoto , name='add'),
]