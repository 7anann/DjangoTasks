from django import forms
from .models import students

class studForm(forms.Form):

    name=forms.CharField(max_length=40,label='Name')
    track = forms.CharField(max_length=20, label='Track')
    class Meta:
        model = students
        fields = '__all__'


class studForm2(forms.ModelForm):

    name=forms.CharField(max_length=40, label='Student Name')
    track=forms.CharField(max_length=20, label="Student Track")

    class Meta:
        model = students
        fields = '__all__'
