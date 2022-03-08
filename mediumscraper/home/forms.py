from django import forms


class NameForm(forms.Form):
    urllink = forms.CharField(label="Article link", widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-sm type-txt',
        }
    ))
