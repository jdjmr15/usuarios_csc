from django.urls import path

from .views import UserCreateView, UserLogin,UserLogoutView


app_name = 'users_app'
urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('profile/', UserProfileView.as_view(), name='profile'),
]