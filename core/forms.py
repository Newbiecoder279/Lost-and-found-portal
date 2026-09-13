from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from accounts.models import User
from item.models import Item
from django import forms
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','phone','college_id','password1','password2']


class ReportItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','category','description','image','item_type','location','date_occurred']

        widgets = {
            'date_occurred': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
        }