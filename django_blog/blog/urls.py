from django.urls import path
from .views import (
    BasePreview, PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    UserLoginView, UserLogoutView, register, profile
)

urlpatterns = [
    # Homepage
    path("", BasePreview.as_view(), name="home"),

    # Post CRUD (checker expects singular 'post')
    path("post/", PostListView.as_view(), name='post-list'),
    path("post/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("post/new/", PostCreateView.as_view(), name='post-create'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),

    # Authentication
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
]
