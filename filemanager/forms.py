from django import forms


class DirectoryCreateForm(forms.Form):
    directory_name = forms.CharField()


class RenameForm(forms.Form):
    input_name = forms.CharField()
    old_name = forms.CharField()
