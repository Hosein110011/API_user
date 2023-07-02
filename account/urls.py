from django.urls import path
from .views import CreatView, LoginView, IdentifyView, DetailView, AccountListView



urlpatterns = [
    path('signup', CreatView.as_view(), name = 'signup'),
    path('login',LoginView.as_view(), name = 'login'),
    path('otp', IdentifyView.as_view(), name = 'otp'),
    path('detail/<int:user_id>', DetailView.as_view(), name= 'detail'),
    path('list', AccountListView.as_view(), name ='list'),
    
]
