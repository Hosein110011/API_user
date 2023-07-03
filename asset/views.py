from django.shortcuts import render
from .serializers import FileUrlSerializer, UploadSerializer
from rest_framework.response import Response
# from rest_framework.status import status
from .models import Asset
from rest_framework.decorators import APIView
from rest_framework.viewsets import ViewSet



class FileUrlView(APIView):
    def post(self, request):
        files = Asset.objects.all()
        serialize = FileUrlSerializer(files,many=True, context = {'request':request})
        
        return Response(serialize.data)
       
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")
    
    def create(self, request):
        asset_id = request.POST.get('asset_id')
        upload_file = request.FILES.get('upload_file')
        file_type = request.POST.get('file_type')
        content = request.POST.get('content')
        new = Asset.objects.create(asset_id=asset_id, upload_file=upload_file, file_type=file_type, content=content)
        new.save()
        serialize = UploadSerializer(new, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response("BAD")