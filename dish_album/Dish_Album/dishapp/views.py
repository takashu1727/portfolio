from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Dishes
from datetime import datetime
from .forms import DishCreateForm, DishUpdateForm
from accounts.models import Users
from django.urls import reverse_lazy
import os
# Create your views here.

class HomeLoginView(LoginRequiredMixin,TemplateView):
    template_name = os.path.join('dish_album', 'dish_home.html')

class DishCreateView(LoginRequiredMixin,CreateView):
    template_name = os.path.join('dish_album', 'dish_create.html')
    form_class = DishCreateForm

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        messages.success(self.request, '料理が登録されました。')
        return super().form_valid(form)
    
class DishListView(LoginRequiredMixin, ListView):
    model = Dishes
    template_name = os.path.join('dish_album', 'dish_list.html')


    def get_queryset(self):
        #querysetにログインしているユーザが登録した料理のみ表示させる
        queryset = Dishes.objects.filter(user_id = self.request.user)
        #search_dish_nameに検索した文字を代入する。
        search_dish_name = self.request.GET.get('dish_name')#getの中身は、dish_list.htmlのinputタグのnameが入る
        search_shop_name = self.request.GET.get('shop_name')
        if search_dish_name:
            #queryに文字があった場合、querysetに条件を追加する（dish_nameの中にqueryの文字が一つでもあるかどうか）
            queryset = queryset.filter(dish_name__icontains=search_dish_name)
        if search_shop_name:
            queryset = queryset.filter(shop_name__icontains=search_shop_name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish_name'] = self.request.GET.get('dish_name', '')
        context['shop_name'] = self.request.GET.get('shop_name', '')
        context['mydish'] = Dishes.objects.filter(user_id = self.request.user)
        return context

class DishUpdateView(LoginRequiredMixin, UpdateView):
    model = Dishes
    form_class = DishCreateForm
    template_name = os.path.join('dish_album', 'dish_edit.html')
    success_url = reverse_lazy('dishapp:dish_list')

    def get_queryset(self):
        queryset = Dishes.objects.filter(user_id = self.request.user)
        return queryset
    
    def form_valid(self, form):
        messages.success(self.request, '料理を更新しました。')
        return super().form_valid(form)
    
class DishDetailView(LoginRequiredMixin, DetailView):
    model = Dishes
    template_name = os.path.join('dish_album', 'dish_detail.html')

    def get_queryset(self):
        queryset = Dishes.objects.filter(user_id = self.request.user)
        return queryset
    
class DishDeleteView(LoginRequiredMixin, DeleteView):
    template_name = os.path.join('dish_album', 'dish_delete.html')
    model = Dishes
    success_url = reverse_lazy('dishapp:dish_list')

def page_not_found_view(request, exception):
    return render(request, 'dish_album/404.html', status=404)