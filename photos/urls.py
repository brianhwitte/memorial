from django.conf.urls import url
from django.contrib import admin
from .views import PicturesView, UploadView

urlpatterns = [
    url(r'^new/$', UploadView.as_view(), name='upload'),
    
    url(r'^$', PicturesView.as_view(), name='pictures'),
    ]
