from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def list_posts(request):
    posts=Post.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
    return render(request,'blogapp/list_posts.html',{'posts':posts})

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blogapp/post_detail.html',{'post':post})

@login_required
def new_post(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            #post.date_published = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm()
    return render(request,'blogapp/edit_post.html',{'form':form})

@login_required
def edit_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid:
            post=form.save(commit=False)
            post.author=request.user
            #post.date_published=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'blogapp/edit_post.html',{'form':form})

@login_required
def post_draft_list(request):
    posts=Post.objects.filter(date_published__isnull=True).order_by('date_created')
    return render(request,'blogapp/post_draft_list.html',{'posts':posts})

@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)      #doubt here !!!!!
    post.publish()
    return redirect('post_detail',pk=post.pk)

@login_required
def delete_post(request,pk):
    post=get_object_or_404(Post,pk=post.pk)     #doubt here !!!!!
    post.delete()
    return redirect('list_posts')
