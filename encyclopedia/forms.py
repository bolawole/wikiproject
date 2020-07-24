from django import forms

class Newentry(forms.Form):
    title= forms.CharField(label='Title',label_suffix="")
    content=forms.CharField(widget=forms.Textarea, label="content",label_suffix="")