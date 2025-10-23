from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

# @api_view()    #by default it would be get method
# def index(request):
#     return Response({'msg': 'Hello World'})


# @api_view(['GET'])          #another way of using get method
# def index(request):
#     return Response({'msg': 'Hello World'})

#Using get and post method in the same method.
# @api_view(['GET','POST'])
# def index(request):
#     if request.method == "GET":
#         return Response({'msg': 'This is GET Request'})
    
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg': 'This is POST Request'})

#Performing CRUD using DRF
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            stud = Student.objects.get(id=id)
            serializer = StudentSerializer(stud)
            return Response(serializer.data)
        stud = Student.objects.all()
        serializer = StudentSerializer(stud, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'})
        return Response(serializer.errors)
    

    if request.method == "PUT":
        id = pk
        student = Student.objects.get(pk=id )
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated!'})
        return Response(serializer.errors)
    
    if request.method == "PATCH":
        id = pk
        student = Student.objects.get(pk=id )
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated!'})
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        id = pk
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({'msg': 'Data Deleted'})