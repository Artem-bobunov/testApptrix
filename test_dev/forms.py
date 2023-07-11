from django.contrib.auth.models import User
from .models import ImageUsers
from django import forms

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя')
    first_name = forms.CharField(label='Введите имя')
    last_name = forms.CharField(label='Введите фамилию')
    email = forms.CharField(label='Введите почту')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password','repeat_password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

class UserRegisterFields(forms.ModelForm):
    pol = forms.CharField(label='Выберите пол',choices=ImageUsers.choices_pol,widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ImageUsers
        fields = ('pol')

