from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('main_menu/', views.main_menu, name='main_menu'),
    path('authenticate/', views.authenticate, name='authenticate'),
    path('logout/', views.logout_view, name='logout'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('deposit/', views.deposit, name='deposit'),
    path('change_pin/', views.change_pin, name='change_pin'),
]


