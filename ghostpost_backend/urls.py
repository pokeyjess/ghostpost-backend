from django.contrib import admin
from django.urls import path, include
from api import views as api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"post", api_views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
