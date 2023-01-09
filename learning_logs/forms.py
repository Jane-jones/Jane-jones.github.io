#-*- coding = utf-8 -*-
#@Time : 2023/1/7 10:16
#@Author : 马卓然
#@File : forms.py.py
#@Software : PyCharm

from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}