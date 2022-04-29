from django.shortcuts import render
# Create your views here.
from authentication.helper import response_object
from . models import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import *
from django.contrib.auth import login

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        response_obj = response_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_obj.set_response(
                data={
                    "user": UserSerializer(user, context=self.get_serializer_context()).data,
                    "token": AuthToken.objects.create(user)[1]
                    },
                success="Signup successfully", autohide=True, show=True, type="success", heading="Successfull",
                description="Your account has been created Successfully")
            return Response(response_obj.get_response())
        else:
            response_obj.set_response(
                data=serializer.errors,
                success="Signup successfully", autohide=True, show=True, type="error", heading="Failed",
                description="<br>".join(["<br>".join(v) for i,v in  serializer.errors.items()]))
            return Response(response_obj.get_response())
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        response_obj = response_object()
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        AuthToken.objects.filter(user=user).delete()
        token = AuthToken.objects.create(user=user)
        url = request.scheme + '://' + request.get_host()
        response_obj.set_response(
            data={'token': token[1], "username": user.username,
                  "email": user.email, "firstname": user.first_name,"id":user.id,
                  "lastname": user.last_name, },
            success="Login successfully",autohide=True,show=True,type="success",heading="Successfull",description="You have successfully loged in")
        return Response(response_obj.get_response())
