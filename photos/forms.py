from django import forms

from multiupload.fields import MultiFileField

from .models import Comment


class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=100, max_file_size=2048*2048*5)
    

class DescriptionForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment', 'author']
