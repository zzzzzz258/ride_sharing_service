from django.urls import path

from . import views


app_name = 'app'
urlpatterns = [
    path("", views.index, name = 'index'),
    path('login', views.log_in, name = 'login'),
    path('login/', views.log_in, name = 'login'),
    path('logout', views.log_out, name = 'logout'),
]
    