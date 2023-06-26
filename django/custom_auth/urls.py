from django.conf.urls import include
from django.urls import path


from . import views

urlpatterns = [
    # signup (or) registration
    path('signup', views.SignupView.as_view(), name='signup'), # POST

    # login & logout
    path('login', views.LoginView.as_view(), name='login'), # POST
    path('logout', views.LogoutView.as_view(), name='logout'), # POST
]   
