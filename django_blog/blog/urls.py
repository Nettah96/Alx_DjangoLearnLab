from django.urls import path
from .views import (
    BasePreview, PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    UserLoginView, UserLogoutView, register, profile
)

urlpatterns = [
    # Homepage
    path("", BasePreview.as_view(), name="home"),

    # Post CRUD
    path("posts/", PostListView.as_view(), name='post-list'),
    path("posts/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("posts/new/", PostCreateView.as_view(), name='post-create'),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name='post-update'),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),

    # Authentication
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
]
