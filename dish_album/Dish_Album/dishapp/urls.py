from django.urls import path
from .views import (HomeLoginView, DishCreateView, DishListView, DishUpdateView,
                    DishDetailView, DishDeleteView
                    )

app_name = 'dishapp'

urlpatterns = [
    path('dish_home/', HomeLoginView.as_view(), name='dish_home'),
    path('dish_create/', DishCreateView.as_view(), name='dish_create'),
    path('dish_list/', DishListView.as_view(), name='dish_list'),
    path('dish_detail/<int:pk>', DishDetailView.as_view(), name='dish_detail'),
    path('dish_edit/<int:pk>', DishUpdateView.as_view(), name='dish_edit'),
    path('dish_delete/<int:pk>', DishDeleteView.as_view(), name='dish_delete'),
]

