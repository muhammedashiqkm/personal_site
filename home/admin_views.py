from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Post, Category, Tag
from .forms import PostForm, CategoryForm, TagForm

@login_required
def admin_dashboard(request):
    context = {
        'active_tab': 'dashboard',
        'post_count': Post.objects.count(),
        'category_count': Category.objects.count(),
        'tag_count': Tag.objects.count(),
        'recent_posts': Post.objects.all()[:5]
    }
    return render(request, 'admin/dashboard.html', context)

@login_required
def admin_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    context = {
        'active_tab': 'posts',
        'posts': posts
    }
    return render(request, 'admin/posts.html', context)

@login_required
def admin_post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_posts')
    else:
        form = PostForm()
    
    context = {
        'active_tab': 'posts',
        'form': form,
        'title': 'Create New Post'
    }
    return render(request, 'admin/post_form.html', context)

@login_required
def admin_post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('admin_posts')
    else:
        form = PostForm(instance=post)
    
    context = {
        'active_tab': 'posts',
        'form': form,
        'title': 'Edit Post',
        'post': post
    }
    return render(request, 'admin/post_form.html', context)

@login_required
def admin_post_delete(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def admin_categories(request):
    categories = Category.objects.all()
    context = {
        'active_tab': 'categories',
        'categories': categories
    }
    return render(request, 'admin/categories.html', context)

@login_required
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_categories')
    else:
        form = CategoryForm()
    
    context = {
        'active_tab': 'categories',
        'form': form,
        'title': 'Create New Category'
    }
    return render(request, 'admin/category_form.html', context)

@login_required
def admin_category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('admin_categories')
    else:
        form = CategoryForm(instance=category)
    
    context = {
        'active_tab': 'categories',
        'form': form,
        'title': 'Edit Category',
        'category': category
    }
    return render(request, 'admin/category_form.html', context)

@login_required
def admin_category_delete(request, category_id):
    if request.method == 'POST':
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def admin_tags(request):
    tags = Tag.objects.all()
    context = {
        'active_tab': 'tags',
        'tags': tags
    }
    return render(request, 'admin/tags.html', context)

@login_required
def admin_tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_tags')
    else:
        form = TagForm()
    
    context = {
        'active_tab': 'tags',
        'form': form,
        'title': 'Create New Tag'
    }
    return render(request, 'admin/tag_form.html', context)

@login_required
def admin_tag_edit(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('admin_tags')
    else:
        form = TagForm(instance=tag)
    
    context = {
        'active_tab': 'tags',
        'form': form,
        'title': 'Edit Tag',
        'tag': tag
    }
    return render(request, 'admin/tag_form.html', context)

@login_required
def admin_tag_delete(request, tag_id):
    if request.method == 'POST':
        tag = get_object_or_404(Tag, id=tag_id)
        tag.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
