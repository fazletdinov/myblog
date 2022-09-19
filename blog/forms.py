from django import forms
from .models import Comments, Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label="Имя")
    email = forms.EmailField(label="Адрес электронной почты")
    to = forms.EmailField(label="Адрес получателя")
    comments = forms.CharField(required=False, widget=forms.Textarea, label="Комментарии")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск')

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'body', 'publish', 'status', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'body': forms.Textarea(attrs={'cols': 60, 'rows': 10}),

        }
class LoginUserForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']