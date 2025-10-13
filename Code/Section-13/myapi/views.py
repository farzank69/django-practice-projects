from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentSerializer
from .models import Student
import io
# Create your views here.
# Deserialization Process (create, update, or delete)
# JSON data -> Python data types -> validates -> complex data(queryset, model instances)    
# POST Method
@csrf_exempt
def read_student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student_data = Student.objects.get(id=id)
            serializer = StudentSerializer(student_data)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='applications/json')
        
        student_data = Student.objects.all()
        serializer = StudentSerializer(student_data, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=python_data, partial=True)     #Updating Partially like name and city only
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': 'Data Updated!'
            }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')