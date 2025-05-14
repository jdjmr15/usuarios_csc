from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect 
from .forms import UserRegisterForm, UserLoginForm
from .models import User

class UserCreateView(FormView):
    template_name = 'users/create_users.html'
    form_class = UserRegisterForm
    success_url = '/users/login/'
    
    def form_valid(self, form):
        
        # Save the user instance
        User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )
        
        # Optionally, you can log the user in after registration
        # login(self.request, user)
        
        return super().form_valid(form)
    


class UserLogin(FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home_app:index')


    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            # Log the user in
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid username or password")
            return self.form_invalid(form)
        
class UserLogoutView(View):
   
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('users_app:login'))