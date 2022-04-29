# import django_filters
# from django_filters.rest_framework import DjangoFilterBackend
# # Create your views here.
# from rest_framework import generics
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.parsers import (
#     JSONParser,
#     MultiPartParser,
#     FileUploadParser,
#     FormParser,
# )
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from datetime import datetime
# from authentication.helper import response_object
# from .serializers import *
# from .models import *
# import datetime
# from django.utils import timezone

# @api_view(['POST'])
# def CreateSchool(request):
#     response_obj = response_object()
#     serializer = schoolSerilizer(data=request.data)
#     if serializer.is_valid():
#         # serializer = productSerilizer(data=request.data)
#         print("insideserializer")
#         serializer.save()
#         response_obj.set_response(
#             data=serializer.data,
#             success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
#             description="Product added successfuly")
#         return Response(response_obj.get_response())
#     else:
#         print("else")
#         return Response(serializer.errors)

# # @api_view(['POST'])
# # def Createimages(request):
# #     serializer = imageSerilizer(data=request.data)
# #     if serializer.is_valid():
# #         # serializer = productSerilizer(data=request.data)
# #         print("insideserializer")
# #         serializer.save()
# #         return Response(serializer.data)
# #     else:
# #         print("else")
# #         return Response(serializer.errors)

# # @api_view(['POST'])
# # def Updateproduct(request, pk):
# #    products = Product.objects.get(id= pk)
# #    serializer = productSerilizer(instance=products,data=request.data)
# #    if serializer.is_valid():
# #        serializer.save()
# #    return Response(serializer.data)
# # @api_view(["DELETE"])
# # def delleteproduct(request, pk):
# #     products = Product.objects.get(id= pk)
# #     Product.delete()
# #     return Response("item delete successfully!")

# # @api_view(['GET'])
# # def ShowAll(request):
# #     response_obj = response_object()
# #     products_=Product.objects.all()
# #     serializer = productsSerilizer(products_, many=True)
# #     response_obj.set_response(
# #         data=serializer.data,
# #         success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
# #         description="Products Fetch successfully")
# #     return Response(response_obj.get_response())

# # @api_view(['POST'])
# # def CreateMedicine(request):
# #  response_obj = response_object()
# #  serializer = productSerilizer(data=request.data)
# #  if serializer.is_valid():
        
# #         print("insideserializer")
# #         serializer.save()
# #         response_obj.set_response(
# #             data=serializer.data,
# #             success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
# #             description="Product added successfuly")
# #         return Response(response_obj.get_response())
# #  else:
# #             return Response(serializer.errors)


# # @api_view(['POST'])
# # def GetMedicine(request):
# #     product_ =Product.objects.filter(disease__name=request.data.get("disease") )
# #     serializer = productSerilizer(product_, many=True)
# #     response_obj = response_object()
# #     response_obj.set_response(
# #         data=serializer.data,
# #         success="Fetched successfully", autohide=True, show=False, type="success", heading="Successfull",
# #         description="Product added successfuly")
# #     return Response(response_obj.get_response())

