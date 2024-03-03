from django.shortcuts import render
from .models import Post

from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'autofocus':'autofocus', 'autocomplete':'off', 'class':'form-control', 'id':'id_title', 'placeholder':'Doc title...'}),
            'content': forms.Textarea(attrs={'rows':15, 'cols':20, 'autocomplete':'off', 'class':'form-control', 'id':'id_content', 'placeholder':'start writing...'})
        }

# Create your views here.
def index(request):
    return render(request, 'app1/index.html', {
        'form': PostForm()
    })