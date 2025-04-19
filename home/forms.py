from django import forms
from .models import Post, Category, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'image', 'category', 'tags', 'is_published']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'rich-text-editor'}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
            'tags': forms.SelectMultiple(attrs={'class': 'select2'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3})
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
