from django import forms


class InputForm1(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)

class InputForm2(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    age = forms.IntegerField()
    dob = forms.DateField(widget = forms.DateField())
    gender = forms.ChoiceField(
        choices = [
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        ]
    )
    address = forms.ChoiceField(widget = forms.TelInput)
    profile_field = forms.ImageField()
    website = forms.URLField(required = False)
    agree = forms.BooleanField

from .models import Blogpost

class Blogpostform(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = "__all__"


from .models import Customer
class CustomerForm(forms.ModelForm):
    class Meta:
            model = Customer
            fields = ['phone', 'address']

class LoginForm(forms.Form):
     username = forms.CharField(max_length=50)
     password = forms.CharField(widget=forms.PasswordInput)
     