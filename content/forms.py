from django import forms

from content.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'phone', 'comment')
