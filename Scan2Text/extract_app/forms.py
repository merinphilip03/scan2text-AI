from django import forms
from .models import UploadedDocs


class DocumentForm(forms.ModelForm):

    class Meta:
        model = UploadedDocs
        fields = ['title', 'file']