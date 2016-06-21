from django import forms

from multiupload.fields import MultiFileField


class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=100, max_file_size=2048*2048*5)
    