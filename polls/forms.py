from django import forms
from django.forms import widgets
from .models import Poll, Choice

class PollAddForm(forms.ModelForm):

    choice1 = forms.CharField(max_length=150, min_length=1, label='Choice 1',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    choice2 = forms.CharField(max_length=150, min_length=1, label='Choice 2',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    choice3 = forms.CharField(max_length=150, min_length=1, label='Choice 3',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    choice4 = forms.CharField(max_length=150, min_length=1, label='Choice 4',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Poll
        fields = ['text', 'choice1', 'choice2', 'choice3', 'choice4']  # Ensure 'choice4' is added here
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }


class EditPollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ['text', ]
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20})
        }


class EditChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', ]
        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-control'})
        }


class ChoiceAddForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', ]
        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-control', })
        }
