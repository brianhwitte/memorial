from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import UploadForm, DescriptionForm
from .models import Picture, Comment
from .photo_methods import image_process
# Create your views here.


class DescriptionView(ListView):

    template_name = 'photos/description.html'
    # model = Comment

    def get_queryset(self):
        pic_id = self.kwargs.get('pk')
        print "pic_id", pic_id
        return Comment.objects.filter(for_picture=pic_id)


class NewDescription(FormView):
    # make success_url the description url for that pic id, and text returned is appended to description
    template_name="new_description"
    form_class = DescriptionForm

    def get_success_url(self):
        pk = self.object.id
        return reverse_lazy('description', kwargs={"pk": pk})


class UploadView(FormView):
    # source: https://github.com/Chive/django-multiupload/blob/master/examples/simple/templates/form.html
    
    template_name = 'photos/upload.html'
    form_class = UploadForm
    success_url = reverse_lazy('upload')

    def form_valid(self, form):

        for each in form.cleaned_data['attachments']:
            
            upload_path, thumb_path = image_process(each)

            Picture.objects.create(url = upload_path, thumb = thumb_path)

        return super(UploadView, self).form_valid(form)


class PicturesView(ListView):
    template_name = 'photos/pictures5.html'
    model = Picture
