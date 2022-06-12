from django.urls import path
from backend import views

boosts_list = views.BoostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

boosts_details = views.BoostViewSet.as_view({
    'put': 'update', # обновить все поля заметки
})

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('call_click/', views.call_click, name='call_click'),
    path('logout/', views.user_logout, name='logout'),
    path('boosts/', boosts_list, name='boosts'),
    path('boosts/<int:pk', boosts_list, name='boosts'),
]
