from django import forms
from .models import Note

class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={'placeholder' : 'Enter note title'}),
            'content' : forms.Textarea(attrs={'rows':6, 'placeholder' : "Enter the note"})
        }
