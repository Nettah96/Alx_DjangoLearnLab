from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']  # Change these fields to match your Book model

        # Optional: Add widgets or labels for better UX and security
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'description': 'Short Description',
        }
