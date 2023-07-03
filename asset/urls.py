from django.urls import path, include
from .views import FileUrlView, UploadViewSet
# from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")


urlpatterns = [
    path('file_url', FileUrlView.as_view(), name = 'file_url'),
    # path('upload', UploadFileView.as_view({'get':'upload'}), name='upload'),
    path('',include(router.urls)),
]
