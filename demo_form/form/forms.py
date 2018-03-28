from django import forms
from django.forms import ModelForm

from demo_form.models import Authorform


class AuthorFormOne(forms.Form):
    name = forms.CharField(max_length=40,label='名称')
    email = forms.EmailField()
    seninformation = forms.CharField(widget=forms.TextInput)

class AuthorFormTwo(ModelForm):
    class Meta:
        model = Authorform
        fields = ('name',)  # 只显示 model 中指定的字段