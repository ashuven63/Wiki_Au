from django.conf.urls import patterns,url
from myRecordUpload import views
urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	
	
	)