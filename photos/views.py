from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, FormMixin, BaseCreateView
from django.views.generic.list import ListView

from .forms import UploadForm, CommentForm
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


class NewComment(CreateView):
    # make success_url the description url for that pic id, and text returned is appended to description
    template_name="photos/new_comment.html"
    form_class = CommentForm

    def get_initial(self):
         initial = super(NewComment, self).get_initial()

         initial['for_picture'] = self.kwargs['photo_id']
         print "for picture", initial['for_picture']
         return initial

    def get_success_url(self):
        pk = self.kwargs['photo_id']
        print "success_pk", pk
        
        return reverse_lazy('description', kwargs={"pk": pk})

    def get(self, request, *args, **kwargs):
        self.object = None
        
        return super(BaseCreateView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(NewComment, self).get_context_data(**kwargs)
        print "context", context
        context['photo_id'] = self.kwargs['photo_id']

        return context


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
