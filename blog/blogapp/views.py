from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from django.utils import timezone
from .forms import PostForm,CommentForm
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

def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'blogapp/add_comment_to_post.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.delete()
    return redirect('post_detail',pk=comment.post.pk)
