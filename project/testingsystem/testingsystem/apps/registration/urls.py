from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index')
]
