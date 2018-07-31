from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post

def home(request):
	return render(request,'blog/home.html')

def blog_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/blog_list.html', {'posts': posts})

def blogpost(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request, 'blog/blogpost.html', {'post': post})

def newpost(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blogpost', pk = post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/editpost.html', {'form': form} )


def editpost(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance= post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blogpost', pk = post.pk)
	else:
		form = PostForm(instance = post)
	return render(request, 'blog/editpost.html', {'form': form} )




