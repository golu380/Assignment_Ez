from rest_framework import serializers;
from api.serializer.user_auth_serializer import *
from User_auth.models import *;

from rest_framework.response import Response

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth.hashers import make_password,check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout
from rest_framework import permissions
from django.contrib.auth.models import User


#Generate Token Manually

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }
    
    
# Registration

class newuserRegistrationView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        password = request.data['password']
        length_pass = len(password)
        cpassword = request.data['Cpassword']
        username = request.data['username']
        
        if(length_pass < 6):
            raise serializers.ValidationError("Password must be greater than 6 charcters")
        
        user = User.objects.filter(username = username)
        if(user):
            raise serializers.ValidationError("User already exists")
        
        if(password != cpassword):
            raise serializers.ValidationError("Password not match")
        encryption = make_password(password)
        print(encryption)
        # request.data._mutable = True
        request.data.update({'password':encryption})
        serializer = newuserregisterSerializer(data = request.data)
        print(serializer)
        
        
        if(serializer.is_valid(raise_exception=True)):
            data = serializer.save()
            token = get_token_for_user(data)
            return Response({'token':token,'msg':'Registration Successfull'},status = status.HTTP_201_CREATED)
        


class newuserLoginView(APIView):
  permission_classes = [IsAuthenticated]
  #renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = newuserloginrSerializer(data=request.data)
    print(serializer)
    # if serializer.is_valid(raise_exception=True):

    username=request.data['username']
    password=request.data['password']
    print(username,password)
    user=User.objects.get(username=username)
    print(user)
    username_database=user.username
    password_database=user.password

    flag=check_password(password,password_database)    #PASSWORD CHECK
    flag=check_password(password,password_database)    #PASSWORD CHECK
    print(flag)

    if (username==username_database and flag==True ):    #flag==True
        request.session['email']=user.email
        request.session['username']=user.username
        # request.session['phone']=user.phone
        # print(request.session['name'])
        # print(request.session['email'])
        # print(request.session['phone'])
        token = get_token_for_user(user)
        return Response({'token':token, 'msg':'Login Success','id':user.id,'email':user.email}, status=status.HTTP_200_OK)
    else:
        return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        

# myapp/views.py
#check the isAdminOrOwner or not

class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user

