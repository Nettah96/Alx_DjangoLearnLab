from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book
urlpatterns += [
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
]

urlpatterns = [
    path('', views.book_list, name='book_list'),

    # ✅ Login and Logout URLs using built-in Django views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # ✅ Registration View
    path('register/', views.register, name='register'),
]
urlpatterns = [
    path('books/add/', add_book, name='add_book'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),
]
