from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import Project
from .serializers import SpecialProjectSerializer
from rest_framework.response import Response


class SpecialProjectView(APIView):
    def post(self, request):
        begin = int(request.data['begin'])
        end = int(request.data['end'])
        projects = Project.objects.all()[begin:end]
        serialize = SpecialProjectSerializer(projects, many=True)
        return Response(serialize.data)
        # return Response({"detail":"nothing"})


