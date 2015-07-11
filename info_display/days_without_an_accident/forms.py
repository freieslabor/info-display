from django import forms
from suit_ckeditor.widgets import CKEditorWidget


class AccidentForm(forms.ModelForm):
    description = forms.CharField(
        required=False,
        widget=CKEditorWidget()
    )
