from django.shortcuts import render
from .serializers import FileUrlSerializer, UploadFileSerializer
from rest_framework.response import Response
# from rest_framework.status import status
from .models import Asset
from rest_framework.decorators import APIView
from rest_framework import viewsets



class FileUrlView(APIView):
    def post(self, request):
        files = Asset.objects.all()
        serialize = FileUrlSerializer(files,many=True, context = {'request':request})
        
        return Response(serialize.data)
       

class UploadFileView(viewsets.ViewSet):
    def post(self, request):
        asset_id = request.data['asset_id']
        upload_file = request.FILES.get('upload')
        file_type = request.data['file_type']
        content = request.data['content']
        new_asset = Asset(asset_id = asset_id, upload_file = upload_file, file_type = file_type ,content = content)
        new_asset.save()
        serialize = UploadFileSerializer(new_asset, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        print(serialize.data)
        return Response({'detail':'not valid'})