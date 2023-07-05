from django.urls import path
from .views import SpecialProjectView



urlpatterns = [
    path('special/', SpecialProjectView.as_view(), name = 'special-projects')
]
