from rest_framework.serializers import Serializer, FileField
from rest_framework import serializers
from .models import Asset



class FileUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['upload_file']
        

class UploadFileSerializer(Serializer):
    upload_file = FileField()
    class Meta:
        model = Asset
        fields = ["asset_id", 'upload_file', 'type_file', 'content']
        