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
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == "GET":
        id = request.data.get('id')
        if id is not None:
            stud = Student.objects.get(id=id)
            serializer = StudentSerializer(stud)
            return Response(serializer.data)
        stud = Student.objects.all()
        serializer = StudentSerializer(stud)
        return Response(serializer.data, many=True)
