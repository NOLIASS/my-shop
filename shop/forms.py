from django import forms
from .models import Newsletter, ProductRating


class NewsletterForm(forms.ModelForm):
    class Meta:
        model  = Newsletter
        fields = ['name', 'email']
        widgets = {
            'name':  forms.TextInput(attrs={
                'placeholder': "Ваше ім'я",
                'class': 'form-input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ваш Email',
                'class': 'form-input'
            }),
        }


class RatingForm(forms.Form):
    score = forms.ChoiceField(
        choices=[(i, f"{'⭐' * i}") for i in range(1, 6)],
        widget=forms.RadioSelect(attrs={'class': 'rating-radio'})
    )