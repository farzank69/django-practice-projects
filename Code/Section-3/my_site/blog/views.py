from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def starting_post(request):
    return HttpResponse("Hello, world. You're at the blog index.")


def posts(request):
    return HttpResponse("Hello, world. You're at the blog posts.")  

def post_detail(request, slug):
    return HttpResponse(f"Hello, world. You're at the blog post: {slug}.")
