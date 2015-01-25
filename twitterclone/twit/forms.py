from django import forms
from models import twit


class twitform(forms.ModelForm):

    class Meta:

        model = twit
        fields = ('title', 'body', 'twit_date', 'author')

