
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index,  name='index'),
    path('profil/', views.about, {}, name = 'profil'),
    path('login/', views.login_view, name = 'login'),
    path('register/', views.myreg , name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('setting/', views.setting, name='setting')
]