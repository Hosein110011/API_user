# from django.shortcuts import render
from rest_framework import status
from .models import Account
from .serializers import (CreatAccountSerializer, AccountDetailSerializer,
                           LoginAccountSerializer, AccountListSerializer
                           )
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
from rest_framework.permissions import IsAuthenticated
import random

class AccountListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        list = Account.objects.all()
        serialize = AccountListSerializer(list, many=True)
        return Response(serialize.data)


class CreatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        account = CreatAccountSerializer(data = request.data)
        if account.is_valid():
            account.save()
            return Response(account.data)
        return Response({'detail':'not valid'},status=status.HTTP_400_BAD_REQUEST)
    

class DetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            account = Account.objects.get(user_id = user_id)
        except Account.DoesNotExist:
            return Response({'detail':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AccountDetailSerializer(account)
        return Response(serializer.data)
    

class IdentifyView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        phone_number = request.data.get('phone_number')
        try:
            account = Account.objects.get(phone_number = phone_number)
        except Account.DoesNotExist:
            return Response({'detail':'phone_number is not valid'},status=status.HTTP_400_BAD_REQUEST)
        account.otp = random.randint(2345678909800, 9923456789000)
        serialize = LoginAccountSerializer(account, data=request.data)
        if serialize.is_valid():
            serialize.save()
        return Response(serialize.data['otp'])


class LoginView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        a = list(LoginAccountSerializer(Account.objects.all(),many = True).data)
        for i in a:
            if int(request.data["otp"]) == int(i["otp"]):
                return Response({"state":"valid"})
        return Response({"state":"not valid"}, status=status.HTTP_400_BAD_REQUEST)