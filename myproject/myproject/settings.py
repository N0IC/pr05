from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.flatpages import views as flatpages_views

urlpatterns = [
    # ... другие URL-маршруты ...
    path('admin/', admin.site.urls),
    path('admin-page/', login_required(flatpages_views.flatpage), {'url': '/admin-page/'}, name='admin-page'),
]