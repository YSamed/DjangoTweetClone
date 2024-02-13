from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    nicname_input = forms.CharField(label="username" , max_length=50)
    message_input = forms.CharField(label="Message" , max_length=100)


class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["username" , "message"]

