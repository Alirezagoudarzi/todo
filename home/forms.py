from django import forms
from django.forms import ModelForm
from .models import Todo



class CreateTodoForm(forms.Form):
    title=forms.CharField()
    body=forms.CharField()
    created=forms.DateTimeField()


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','body','created']

    