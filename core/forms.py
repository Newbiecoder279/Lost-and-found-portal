from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','phone','college_id','password1','password2']