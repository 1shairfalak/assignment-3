import json
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import (
    JSONParser,
    MultiPartParser,
    FileUploadParser,
    FormParser,
)
from django.db.models import Count
from rest_framework.permissions import AllowAny, IsAuthenticated
from datetime import datetime
from authentication.helper import response_object
from .serializers import *
from .models import *
import datetime
from django.utils import timezone

@api_view(['POST'])
def CreateSchool(request):
    response_obj = response_object()
    serializer = schoolSerilizer(data=request.data)
    if serializer.is_valid():
        # serializer = productSerilizer(data=request.data)
        print("insideserializer")
        serializer.save()
        response_obj.set_response(
            data=serializer.data,
            success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
            description="Product added successfuly")
        return Response(response_obj.get_response())
    else:
        print("else")
        return Response(serializer.errors)

# @api_view(['POST'])
# def Createimages(request):
#     serializer = imageSerilizer(data=request.data)
#     if serializer.is_valid():
#         # serializer = productSerilizer(data=request.data)
#         print("insideserializer")
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         print("else")
#         return Response(serializer.errors)

# @api_view(['POST'])
# def Updateproduct(request, pk):
#    products = Product.objects.get(id= pk)
#    serializer = productSerilizer(instance=products,data=request.data)
#    if serializer.is_valid():
#        serializer.save()
#    return Response(serializer.data)
# @api_view(["DELETE"])
# def delleteproduct(request, pk):
#     products = Product.objects.get(id= pk)
#     Product.delete()
#     return Response("item delete successfully!")

@api_view(['GET'])
def ShowAll(request):
    response_obj = response_object()
    products_=question.objects.all()
    serializer = questionSerilizer(products_, many=True)
    response_obj.set_response(
        data=serializer.data,
        success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
        description="question Fetch successfully")
    return Response(response_obj.get_response())
@api_view(['GET'])
def questionwithdepatmentname(request):
    response_obj = response_object()
    products_=question.objects.all()
    serializer = questionwithdepartmentSerilizer(products_, many=True)
    response_obj.set_response(
        data=serializer.data,
        success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
        description="question with subject name and description Fetch successfully")
    return Response(response_obj.get_response())
@api_view(['GET'])
def questionhierarchy(request):
    response_obj = response_object()
    products_=question.objects.all()
    serializer = questionhierarchySerilizer(products_, many=True)
    response_obj.set_response(
        data=serializer.data,
        success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
        description=" questionhierarchy Fetch successfully")
    return Response(response_obj.get_response())
@api_view(['GET'])
def questionaggregation(request):
    response_obj = response_object()
    
    products_=list(question.objects.values('subject__name').annotate(dcount=Count('statement')))
    print(products_)
    
    response_obj.set_response(
        data=products_,
        success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
        description=" aggregation  Fetch successfully")
    return Response(response_obj.get_response())



@api_view(['POST'])
def tracking(request):
   response_obj = response_object()
   products_=question.objects.filter(subject__id=request.data.get("id"))

   serializer = questionfilterSerilizer(products_, many=True)
   response_obj.set_response(
        data=serializer.data,
        success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
        description=" question subject join Fetch successfully")
   return Response(response_obj.get_response())
    
# @api_view(['POST'])
# def CreateMedicine(request):
#  response_obj = response_object()
#  serializer = productSerilizer(data=request.data)
#  if serializer.is_valid():
        
#         print("insideserializer")
#         serializer.save()
#         response_obj.set_response(
#             data=serializer.data,
#             success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
#             description="Product added successfuly")
#         return Response(response_obj.get_response())
#  else:
#             return Response(serializer.errors)


# @api_view(['POST'])
# def GetMedicine(request):
#     product_ =Product.objects.filter(disease__name=request.data.get("disease") )
#     serializer = productSerilizer(product_, many=True)
#     response_obj = response_object()
#     response_obj.set_response(
#         data=serializer.data,
#         success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
#         description="Product added successfuly")
#     return Response(response_obj.get_response())

