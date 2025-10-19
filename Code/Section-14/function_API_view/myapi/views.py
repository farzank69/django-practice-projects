from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view()    #by default it would be get method
# def index(request):
#     return Response({'msg': 'Hello World'})


# @api_view(['GET'])          #another way of using get method
# def index(request):
#     return Response({'msg': 'Hello World'})

@api_view(['GET','POST'])
def index(request):
    if request.method == "GET":
        return Response({'msg': 'This is GET Request'})
    
    if request.method == "POST":
        print(request.data)
        return Response({'msg': 'This is POST Request'})