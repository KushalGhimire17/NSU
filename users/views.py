from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MemberForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                x = form.save()
                x.added_by = request.user
                x.save()
            else:
                form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = MemberForm()
    return render(request, 'users/register.html', {'form': form})