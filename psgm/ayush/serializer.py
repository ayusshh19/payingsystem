from dataclasses import fields
from rest_framework import serializers
from .models import login_log, password_history, user_signup, rooms,deleted_account

class signupSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_signup
        fields='__all__'
        
class logSerializer(serializers.ModelSerializer):
    class Meta:
        model=login_log
        fields='__all__'
        
class roomSerializer(serializers.ModelSerializer):
    class Meta:
        model=rooms
        fields='__all__'
        
class passSerializer(serializers.ModelSerializer):
    class Meta:
        model=password_history
        fields='__all__'
        
class delSerializer(serializers.ModelSerializer):
    class Meta:
        model=deleted_account
        fields='__all__'