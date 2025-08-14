from django.urls import path
from .views import (
    BasePreview,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    # Home
    path("", BasePreview.as_view(), name="home"),

    # Post CRUD
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # Comment CRUD
    path("post/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comments/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
