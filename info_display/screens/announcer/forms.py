from django import forms
from django.forms import ModelForm
from suit_ckeditor.widgets import CKEditorWidget


class AnnouncementForm(ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
