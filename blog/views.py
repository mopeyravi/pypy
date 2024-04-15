from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Post

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,id=pid) # agar oon id dar database vojood nadasht 404 bargardune
    context = {'post':post}
    return render(request, 'blog/blog-single.html',context)

def test(request,pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post,id=pid) # agar oon id dar database vojood nadasht 404 bargardune
    context = {'post':post}
    return render(request, 'test.html',context)