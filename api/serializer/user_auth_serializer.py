from rest_framework import serializers
# from User_auth.models import *
from django.contrib.auth.models import User


class newuserregisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    Cpassword=serializers.CharField(max_length=255,read_only=True)
    # name = serializers.CharField(max_length= 254)
    class Meta:
        model = User
        fields = ['email','password','Cpassword','username'] 
        
        
class newuserloginrSerializer(serializers.ModelSerializer):
  # email = serializers.EmailField(max_length=255)
  
  class Meta:
    model = User
    fields = ['username', 'password']