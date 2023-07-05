from django.urls import path
from .views import SpecialProjectView



urlpatterns = [
    path('special/<int:begin>&<int:end>/', SpecialProjectView.as_view(), name = 'special-projects')
]
