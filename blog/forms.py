from django import forms
from .models import Comments

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label="Имя")
    email = forms.EmailField(label="Адрес электронной почты")
    to = forms.EmailField(label="Адрес получателя")
    comments = forms.CharField(required=False, widget=forms.Textarea, label="Комментарии")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'body')
