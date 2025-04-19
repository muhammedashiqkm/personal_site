# myapp/urls.py

from django.urls import path
from . import views, admin_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.home, name='home'),
    
    # Blog URLs
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/category/<slug:category_slug>/', views.blog_category, name='blog_category'),
    path('blog/<slug:post_slug>/', views.blog_detail, name='blog_detail'),
    
    # Contact URL
    path('contact/', views.contact, name='contact'),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    
    
    # Admin URLs
    path('admin/', login_required(admin_views.admin_dashboard), name='admin_dashboard'),  
    path('admin/dashboard/', login_required(admin_views.admin_dashboard), name='admin_dashboard'),
    path('admin/posts/', admin_views.admin_posts, name='admin_posts'),
    path('admin/posts/create/', admin_views.admin_post_create, name='admin_post_create'),
    path('admin/posts/<int:post_id>/edit/', admin_views.admin_post_edit, name='admin_post_edit'),
    path('admin/posts/<int:post_id>/delete/', admin_views.admin_post_delete, name='admin_post_delete'),
    
    path('admin/categories/', admin_views.admin_categories, name='admin_categories'),
    path('admin/categories/create/', admin_views.admin_category_create, name='admin_category_create'),
    path('admin/categories/<int:category_id>/edit/', admin_views.admin_category_edit, name='admin_category_edit'),
    path('admin/categories/<int:category_id>/delete/', admin_views.admin_category_delete, name='admin_category_delete'),
    
    path('admin/tags/', admin_views.admin_tags, name='admin_tags'),
    path('admin/tags/create/', admin_views.admin_tag_create, name='admin_tag_create'),
    path('admin/tags/<int:tag_id>/edit/', admin_views.admin_tag_edit, name='admin_tag_edit'),
    path('admin/tags/<int:tag_id>/delete/', admin_views.admin_tag_delete, name='admin_tag_delete'),
]