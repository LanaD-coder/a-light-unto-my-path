"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_views
from accounts.views import custom_logout_view
from django.views.generic import RedirectView
from django.conf.urls import handler404
from accounts.views import custom_404_view

handler404 = custom_404_view

def redirect_to_homepage(request):
    return redirect('homepage')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('homepage/', include('homepage.urls')),
    path('logout/', custom_logout_view, name='logout_page'),
    path('summernote/', include('django_summernote.urls')),
    path('comments/', blog_views.comment_view, name='comment_view'),

    path('', redirect_to_homepage, name='root_redirect'),
    path('quiz/', include('quiz.urls', namespace='quiz')),

]

# Serve files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])