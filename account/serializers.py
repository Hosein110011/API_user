from rest_framework import serializers
from . models import Account


class CreatAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email']


class LoginAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone_number', 'otp']


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number','account_type']

class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name','eamil', 'phone_number', 'account_type']
