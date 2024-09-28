from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def allBlogPosts(request):
    posts = BlogPost.objects.values('id', 'title').order_by('-created_at')
    return render(request, 'blogs/blog_list.html', {'posts': posts})

def blogById(request, id):
    post_id = BlogPost.objects.get(id=id)
    return render(request, 'blogs/blog_detail.html', {'post': post_id})
