from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'genre', 'director', 'year', 'synopsis', 'picture', 'Id']
        widgest= {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie name'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie genre'}),
            'director': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter director name'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter release year'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter movie synopsis'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'Id': forms.HiddenInput(),
        }