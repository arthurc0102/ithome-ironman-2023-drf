"""
URL configuration for server project.

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
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from server.app.common import views as common_views
from server.app.todo import views as todo_views

router = routers.SimpleRouter(trailing_slash=False)
router.register("todo/tasks", todo_views.TaskViewSet)
router.register("todo/tags", todo_views.TagViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health", common_views.HealthView.as_view()),
    path("api/token", jwt_views.TokenObtainPairView.as_view()),
    path("api/token/refresh", jwt_views.TokenRefreshView.as_view()),
    path("api/", include(router.urls)),
]
