from django.conf.urls import url
from django.contrib import admin
from .views import PicturesView, UploadView, DescriptionView, NewComment

urlpatterns = [
    url(r'^new/$', UploadView.as_view(), name='upload'),
    
    url(r'^$', PicturesView.as_view(), name='pictures'),
    url(r'^descriptions/(?P<pk>[0-9]+)/$', DescriptionView.as_view(), name='description'),
    url(r'^descriptions/(?P<photo_id>[0-9]+)/new_comment/', NewComment.as_view(), name="new_comment"),
    ]
