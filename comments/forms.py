from .models import Comment
from django import forms


class AddComment(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Comment
        fields = ('text',)
