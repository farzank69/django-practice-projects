from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.



def starting_post(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]  # Slice to get the latest 3 posts only
    return render(request, 'blog/index.html', {'posts': latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)   # Fetch post by slug or return 404 if not found
    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
        'post_tags': identified_post.tags.all()  # Fetch all tags related to the post
    })
