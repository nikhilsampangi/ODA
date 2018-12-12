from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'blog'

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('make/', views.make, name='make_blog'),
    path('edit/<int:post_id>', views.edit, name='edit_blog'),
    path('delete/<int:post_id>', views.de1, name='delete_blog'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
