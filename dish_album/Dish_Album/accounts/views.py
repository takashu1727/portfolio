from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .forms import RegistForm, UserLoginForm, UserEditForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Users
from dishapp.models import Dishes

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm
    success_url = reverse_lazy('accounts:user_login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '会員登録が完了しました。ログインしてください。')
        return response

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm

class UserLogoutView(LoginRequiredMixin, LogoutView):
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'ログアウトしました。')
        return super().dispatch(request, *args, **kwargs)

class UserEditView(LoginRequiredMixin, UpdateView):
    model = Users
    template_name = 'user_edit.html'
    form_class = UserEditForm
    success_url = reverse_lazy('dishapp:dish_home')
    
    def get_queryset(self):
        query = Users.objects.filter(pk = self.request.user.id)
        return query

    def form_valid(self, form):
        if form.has_changed():#has_changedは、POSTされたデータと既存データに差分があればTrue、なければFalseを返す。
            messages.success(self.request, 'ユーザ情報を更新しました。')
        return super().form_valid(form)