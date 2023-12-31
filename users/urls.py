from users import views as user_views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'users' 
urlpatterns = [
path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
path('accounts/profile/', user_views.profile, name='profile'),

]