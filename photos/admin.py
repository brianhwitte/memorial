from django.contrib import admin
from .models import Picture, Comment, Story
# Register your models here.

admin.site.register(Picture)
admin.site.register(Comment)
admin.site.register(Story)