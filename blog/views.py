from django.shortcuts import render
from .models import Post
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'blog/home.html')

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)

def notice(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'blog/notice.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def read_more(request,id):
    context = {
        'blog': Post.objects.get(pk=id)
    }
    return render(request, 'blog/read_more.html', context) 