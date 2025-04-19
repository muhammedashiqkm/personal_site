from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Post, Tag
import logging

logger = logging.getLogger(__name__)

# Render static pages
def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

# Blog list with categories and recent posts
def blog_list(request):
    categories = Category.objects.all()
    recent_posts = Post.objects.filter(is_published=True)[:6]
    
    context = {
        'categories': categories,
        'recent_posts': recent_posts,
    }
    
    return render(request, 'blog_list.html', context)

# Blog posts by category
def blog_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, is_published=True)
    
    context = {
        'category': category,
        'posts': posts,
    }
    
    return render(request, 'blog_category.html', context)

# Blog detail with next/previous and related posts
def blog_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug, is_published=True)
    
    previous_post = Post.objects.filter(
        created_at__lt=post.created_at,
        is_published=True
    ).order_by('-created_at').first()
    
    next_post = Post.objects.filter(
        created_at__gt=post.created_at,
        is_published=True
    ).order_by('created_at').first()
    
    related_posts = post.get_related_posts()
    
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
        'related_posts': related_posts,
    }
    
    return render(request, 'blog_detail.html', context)

# Contact form handling via AJAX
@csrf_exempt  # Consider removing this and using CSRF tokens properly
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        
        if not all([name, email, message]):
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields.'
            }, status=400)
        
        try:
            send_mail(
                subject=f'New Contact Form Submission from {name}',
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Your message has been sent successfully.'
            })
        
        except Exception as e:
            logger.error(f"Error sending contact form email: {str(e)}")
            return JsonResponse({
                'success': False,
                'message': 'There was an error sending your message. Please try again later.'
            }, status=500)

    return render(request, 'index.html')
