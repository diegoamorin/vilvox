from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('', include('apps.blog.urls')),
    path('', include('apps.events.urls')),
    path('wiki/', include('apps.wiki.urls')),
    path('login/', login, {'template_name':'loginForm.html'}, name='login'),
    path('logout/', logout_then_login, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
