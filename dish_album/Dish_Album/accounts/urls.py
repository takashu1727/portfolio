from django.urls import path
from .views import (RegistUserView, HomeView, UserLoginView, 
                    UserLogoutView, UserEditView
                    )

app_name = 'accounts'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('regist/', RegistUserView.as_view(), name='regist'),
    path('user_logout/', UserLogoutView.as_view(), name='user_logout'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    path('user_edit/<int:pk>', UserEditView.as_view(), name='user_edit'),
]