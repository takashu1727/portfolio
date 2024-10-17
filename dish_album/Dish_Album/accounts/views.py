from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .forms import RegistForm, UserLoginForm, UserEditForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Users

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm

class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass

class UserEditView(LoginRequiredMixin, UpdateView):
    model = Users
    template_name = 'user_edit.html'
    form_class = UserEditForm
    success_url = reverse_lazy('dishapp:dish_home')
    
    def get_queryset(self):
        query = Users.objects.filter(pk = self.request.user.id)
        return query
