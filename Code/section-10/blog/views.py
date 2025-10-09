from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View


from .models import Post
from .forms import CommentForm
# Create your views here.


class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date"]        #can order it by multiple fields in the same list.
    context_object_name = "posts"
    # to query the complete data
    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data


class PostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]
    
    

class PostDetailView(View):
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post-tags": post.tags.all(),
            "comment_form": CommentForm(), 
            "comments": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post 
            comment.save()
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
        
        context = {
            "post": post,
            "post_tags": post.tags.all(), 
            "comment_form": comment_form,
            "comments": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)



