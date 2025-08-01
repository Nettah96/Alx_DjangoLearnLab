from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Create and configure the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Original list-only view (optional if you want to keep it)
    path('books/', BookList.as_view(), name='book-list'),
    path('auth/token/', obtain_auth_token, name='api_token_auth'),
    # Automatically handle all routes for BookViewSet
    path('', include(router.urls)),
]
