from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from app import views
from django.conf.urls.static import static
from django.urls import re_path


urlpatterns = [
    re_path(r'^app/', include('app.urls')),
    re_path(r'^api/', include('api.urls')),
    re_path(r'^logout/$', views.logout_user),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Print banner on the console when the server starts
print(settings.BANNER)

# Custom Admin Site Header
admin.site.site_header = settings.NAME