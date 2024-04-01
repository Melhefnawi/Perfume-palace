from .models import Comment
from django import forms
from .models import Review
from .models import ContactMessage


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['item', 'comment', 'rating']
        labels = {
            'item': 'Item',
            'comment': 'Comment',
            'rating': 'Rating'
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']        