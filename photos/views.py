from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import UploadForm
from .models import Picture
from .photo_methods import image_process
# Create your views here.


class UploadView(FormView):
    # source: https://github.com/Chive/django-multiupload/blob/master/examples/simple/templates/form.html
    
    template_name = 'photos/upload.html'
    form_class = UploadForm
    success_url = reverse_lazy('upload')

    def form_valid(self, form):

        # uploader = self.request.user

        for each in form.cleaned_data['attachments']:
            
            upload_path, thumb_path = image_process(each)

            Picture.objects.create(url = upload_path, thumb = thumb_path)

        return super(UploadView, self).form_valid(form)


class PicturesView(ListView):
    template_name = 'photos/pictures.html'
    model = Picture