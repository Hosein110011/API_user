from rest_framework.serializers import Serializer, FileField
from rest_framework import serializers
from .models import Asset



class FileUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['upload_file']
        

class UploadSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Asset
        fields = ['asset_id','upload_file', 'file_type', 'content']
        