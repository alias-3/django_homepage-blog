from django.shortcuts import render
from django.utils import timezone
from .models import Post

def home(request):
	return render(request,'blog/home.html')

def blog_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/blog_list.html', {'posts': posts})