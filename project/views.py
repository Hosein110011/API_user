from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import Project
from .serializers import SpecialProjectSerializer
from rest_framework.response import Response


class SpecialProjectView(APIView):
    def get(self, request, begin, end):
        begin = int(begin)
        end = int(end)
        projects = Project.objects.all()[begin:end]
        serialize = SpecialProjectSerializer(projects, many=True)
        return Response(serialize.data)
        # return Response({"detail":"nothing"})


