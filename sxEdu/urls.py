from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^uploadOpus/$',views.uploadOpus,name='uploadOpus'),
    url(r'^doUpload/$',views.doUpload,name='doUpload'),
    url(r'^myOpus/$',views.myOpus,name='myOpus'),
    url(r'^othersOpus/$',views.othersOpus,name='othersOpus'),
    url(r'^studentTranscript/$',views.getStudentTranscript,name='getStudentTranscript'),
]

