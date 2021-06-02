from django import forms
from django.forms import ModelForm
from .models import Contact, Quizz, Comment, Musician, Result_Quizz


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        labels = {
            'perm': 'Permission',
        }


class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'


class Result_QuizzForm(ModelForm):
    class Meta:
        model = Result_Quizz
        fields = '__all__'


class QuizzForm(ModelForm):
    choice = (('Yes', 'Yes'), ('No', 'No'))
    question1 = forms.ChoiceField(label='Can I save the parameters as favourites to use them later?', choices=choice,
                                  widget=forms.RadioSelect(attrs={'class': 'question1'}))

    question7 = forms.ChoiceField(label='Can I talk with my friends via chat?', choices=choice,
                                  widget=forms.RadioSelect(attrs={'class': 'question1'}))

    question5 = forms.ChoiceField(label='Can I record my live performances?', choices=choice,
                                  widget=forms.RadioSelect(attrs={'class': 'question1'}))

    question4 = forms.ChoiceField(label='Can I add my own sounds?', choices=choice,
                                  widget=forms.RadioSelect(attrs={'class': 'question1'}))

    class Meta:
        model = Quizz
        fields = '__all__'

        widgets = {

            'question3': forms.TextInput(attrs={'class': 'labels', 'type': 'range', 'min': '1', 'max': '3'}),
        }

        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'email': 'Email',
            'question3': 'How many parameters do I need to play music?',
            'question2': "What's the name of the app?",
            'question8': 'How many effects can I have at the same time?',
            'question9': 'How many people were envolved on the development of this app?',
            'question10': 'When was the app created?',
            'question6': 'How many sensors are available?',

        }
        help_texts = {
            'question3': 'Scale from 1 to 3',
        }


class CommentForm(ModelForm):
    genders = (('Yes', 'Yes'), ('No', 'No'), ('More or less', 'More or less'))
    question1 = forms.ChoiceField(label='Did you enjoy the website?', choices=genders,
                                  widget=forms.RadioSelect(attrs={'class': 'question1'}))
    choices = (('Yes', 'Yes'), ('No', 'No'))
    question5 = forms.ChoiceField(label='Did you find any bugs?', choices=choices,
                                  widget=forms.RadioSelect(attrs={'class': 'question1'}))

    class Meta:
        model = Comment
        fields = '__all__'

        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'email': 'Email',
            'question2': 'Font size',
            'question3': 'Overall screen design',
            'question4': 'Did you find easily what you were looking for?',
            'question6': 'Clarity of the vocabulary used',
            'question7': 'If you could change one thing on the website, what would it be?',
            'question8': 'The used colours allow easy reading',
            'question9': 'Open comment',

        }
