from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from filemanager.views import (BrowserView, DetailView, UploadView,
                               UploadFileView, DirectoryCreateView, RenameView,
                               DeleteView)

app_name= 'filemanager'

urlpatterns = [
    url(r'^$', BrowserView.as_view(), name='browser'),
    url(r'^detail/$', DetailView.as_view(), name='detail'),
    url(r'^upload/$', UploadView.as_view(), name='upload'),
    url(r'^upload/file/$', csrf_exempt(UploadFileView.as_view()), name='upload-file'),
    url(r'^create/directory/$', DirectoryCreateView.as_view(), name='create-directory'),
    url(r'^rename/$', RenameView.as_view(), name='rename'),
    url(r'^delete/$', DeleteView.as_view(), name='delete'),
]