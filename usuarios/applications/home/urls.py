from django.urls import path

from .views import HomeView


app_name = 'home_app'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('profile/', UserProfileView.as_view(), name='profile'),
]