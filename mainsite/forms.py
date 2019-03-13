#-*- encoding:utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    ITEM = [
        ['桌球','桌球'],
        ['羽球','羽球'],
        ['游泳','游泳'],
        ['籃球','籃球'],
        ['棒球','棒球'],
        ['其他','其他'],
    ]
    GROUP = [
        ['低年級組','低年級組'],
        ['中年級組','中年級組'],
        ['高年級組','高年級組'],
    ]
    
    user_item = forms.ChoiceField(label = '項目',choices = ITEM)
    user_group = forms.ChoiceField(label = '組別',choices = GROUP)
    user_name = forms.CharField(label = '姓名',max_length = 50)
    user_name2 = forms.CharField(label = '教練',max_length = 50)
    user_email = forms.EmailField(label = 'Email')
    user_number = forms.CharField(label = '聯絡電話')

class LoginForm(forms.Form):
    
    username = forms.CharField(label = '帳號',max_length = 50)
    password = forms.CharField(label = '密碼',widget = forms.PasswordInput())