from django.shortcuts import render
from .forms import *
from django.views.generic import ListView,DetailView,CreateView
from .models import BlogEdit


# Create your views here.
#first page for user 
def homepage(request):
	blog=BlogEdit.objects.all()
	

	return render(request,'index.html',{'blog': blog})


def edit_blog(request):
	form=BlogForm()
	if request.method=="POST":
		if request.user.is_authenticated:
			username = request.user.username
			blog_title=request.POST['title']
			blog_content=request.POST['blog']
			blog_tag=request.POST['tags']
			
			blogsave=BlogEdit(title=blog_title,blog=blog_content,tags=blog_tag,bloguser=username)
			blogsave.save()

	else:
		form=BlogForm()

	

	return render(request,'blog.html',{'form':form})


def portfolio(request):
	
	return render(request,'portfolio.html')

class PostListView(ListView):
	model=BlogEdit
	template_name='index.html'
	context_object_name='blog'
	
	

class PostDetailView(DetailView):
	model=BlogEdit
	
class PostUpdateView(CreateView):
	model=BlogEdit
	fields=['title','blog','tags']

	def form_valid(self,form):
		form.instance.bloguser=self.request.username
		return super().form_valid(form)