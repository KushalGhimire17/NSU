from django import forms
from .models import Notice, Post

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('title','notice','cover')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'date_posted', 'author')