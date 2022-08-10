# -*-coding:utf-8-*-
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=32, widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': '用户名/邮箱'
    }))
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '密码'
    }))

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username == password:
            raise forms.ValidationError('用户名与密码不能相同！')
        return password


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='邮箱', min_length=6, widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': '用户名/邮箱'
    }))
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '密码'
    }))
    password_retry = forms.CharField(label='再次输入密码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '密码'
    }))

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_email(self):
        """ 验证用户是否存在 """
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('用户名已经存在')
        return email

    def clean_password_retry(self):
        """ 两次输入密码验证 """
        password = self.cleaned_data.get('password')
        password_retry = self.cleaned_data.get('password_retry')
        if password != password_retry:
            raise forms.ValidationError('两次输入密码不一致')
        return password_retry


class ForgetPwdForm(forms.Form):
    """ 填写email表单页面 """
    email = forms.EmailField(label='请输入注册邮箱地址', min_length=4, widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': '用户名/邮箱'
    }))


class ModifyPwdForm(forms.Form):
    """修改密码表单"""
    password = forms.CharField(label="输入新密码", min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '输入密码'}))


class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input', 'disabled': 'disabled'
    }))

    class Meta:
        model = User
        fields = ('email',)


class UserProfileForm(forms.ModelForm):
    """Form definition for UserInfo."""

    class Meta:
        """Meta definition for UserInfoform."""

        model = UserProfile
        fields = ('nike_name', 'desc', 'signature', 'birthday', 'gender', 'address', 'image')
