from django import forms
from .models import Image,Profile

class Form(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user_name', 'pub_date','comment','posting','likes','profiles']
        # widgets = {
        #     'pic': forms.CheckboxSelectMultiple(),
        # }

class UpdateProForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['follower', 'following']

