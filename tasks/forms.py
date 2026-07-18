from django.db import models
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms

from .models import Task, Comment


User = get_user_model()
# # Create your models here.
# class RegisterForm(UserCreationForm):
#     username = forms.CharField(max_length=300,label='username')
#     widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
#                'password': forms.PasswordInput(attrs={'class': 'form-control'})
#                }
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=300,label='username')
#     password = forms.CharField(label='password')
#     widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
#                'password': forms.PasswordInput(attrs={'class': 'form-control'})
#                }
    

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date", "file"]
        widgets = {
            "due_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }


class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(
        choices=[('', 'Усі')] + Task.STATUS_CHOICES,
        required=False,
        label='Статус'
    )

    priority = forms.ChoiceField(
        choices=[('', 'Усі')] + Task.PRIORITY_CHOICES,
        required=False,
        label='Пріоритет'
    )

    due_date = forms.DateField(
        required=False,
        label='Дата виконання',
        widget=forms.DateInput(attrs={'type': 'date'})
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "placeholder": "Напишіть коментар..."}),
        }
