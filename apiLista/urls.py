from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TaskViews

router = DefaultRouter()
router.register(r"tasks", TaskViews)

urlpatterns = [
    path('', include(router.urls)),
]
