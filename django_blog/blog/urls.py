from django.urls import path
from .views import (
    BasePreview, PostListView,
    UserLoginView, UserLogoutView, register, profile
)

urlpatterns = [
    path("", BasePreview.as_view(), name="home"),
    path("posts/", PostListView.as_view(), name="posts"),

    # auth
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
]
