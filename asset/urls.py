from django.urls import path, include
from .views import FileUrlView, UploadFileView
# from rest_framework import routers
from asset.views import UploadFileView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'upload', UploadFileView, basename="upload")


urlpatterns = [
    path('file_url', FileUrlView.as_view(), name = 'file_url'),
    # path('upload', UploadFileView.as_view(), name='upload'),
    path('', include('router.urls')),
]
