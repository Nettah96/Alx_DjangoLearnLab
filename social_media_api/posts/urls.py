from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed
from .views import LikeView, UnlikeView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', feed, name='feed'),
    path('<int:pk>/like/', LikeView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikeView.as_view(), name='unlike-post'),
]
