from django.shortcuts import render, redirect
from .models import Post, Notice
from django.core.files.storage import FileSystemStorage
from .forms import NoticeForm

def home(request):
    return render(request, 'blog/home.html')

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)

def notice(request):
    notice_lists = Notice.objects.all()
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('notice')
    else:
        form = NoticeForm()
    return render(request, 'blog/notice.html', {'notice_lists':notice_lists, 'form':form})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def read_more(request,id):
    context = {
        'blog': Post.objects.get(pk=id)
    }
    return render(request, 'blog/read_more.html', context) 