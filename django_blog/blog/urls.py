from django.urls import path
from .views import BasePreview, PostListView

urlpatterns = [
    path("", BasePreview.as_view(), name="home"),
    path("posts/", PostListView.as_view(), name="posts"),  
]
