"""
URL configuration for setting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from server.account.views import TokenObtainPairView
from server.setting import settings

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/restaurants/', include('restaurant.urls', namespace='restaurant')),
    path('api/user/', include('server.account.urls', namespace='account')),
    path('api/', include_docs_urls(title='API docs')),
    path('api/token/create/', TokenObtainPairView.as_view(), name='token_auth'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_URLS, document_root=settings.MEDIA_URLS)
urlpatterns += static(settings.STATIC_URLS, document_root=settings.STATIC_ROOT)

