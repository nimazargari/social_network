from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_user'),
    path('login/', views.UserLoginView.as_view(), name='login_user'),
    path('logout/', views.UserLogoutView.as_view(), name='logout_user'),
    path('profile/<int:user_id>', views.UserProfileView.as_view(), name='profile_user'),
]