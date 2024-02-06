
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from apk.models import Student
from .serializers import StudentSerializers
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def getdata(request):
    if request.method == "GET":
        
        data = Student.objects.all()
        serializer = StudentSerializers(data, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def data_detail(request, pk):
    try:
        data = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializers(data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializers(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





############# with name find  a person ############

# @api_view(['GET', 'POST'])
# def getdata(request):
#     if request.method == "GET":
#         name = request.query_params.get('name', None)

#         if name:
#             data = Student.objects.filter(name__icontains=name)
#         else:
#             # If 'name' parameter is not provided, return all data
#             data = Student.objects.all()

#         serializer = StudentSerializers(data, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def data_detail(request, pk):
#     try:
#         data = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = StudentSerializers(data)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = StudentSerializers(data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         data.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
