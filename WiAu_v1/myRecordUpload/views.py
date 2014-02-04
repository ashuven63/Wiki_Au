# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from myRecordUpload.soundProcessing import soundProcessWithAuphonic
from myRecordUpload.models import Document
from myRecordUpload.forms import DocumentForm
from django.templatetags.static import static
from myRecordUpload.tasks import soundProcessingWithAuphonicTask
from urllib import urlretrieve


def index(request):
    # Handle file upload
    '''
    Add additional inputs to post to figure out the book and 
    the paragraph number so that the upload takes place in that folder
    Current working : Saves the file with a fixed name and the file sent for API processing is fixed as well. 
    Both of these should be made dynamic 
    '''
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.docfile.save('Ashu.wav',request.FILES['docfile'])
            #soundProcessWithAuphonic('documents/Ashu.wav')
            soundProcessingWithAuphonicTask.delay('../documents/ashu.mp3')
            return HttpResponseRedirect(reverse('myRecordUpload.views.index'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myRecordUpload/index.html',
        {'documents': documents, 'form': form},
       
        context_instance=RequestContext(request)
    )


#def recordedFileURL(request):
#    if request.method == 'POST':
#        audioUrl = REQUEST['urlLink']
    #    soundProcessWithAuphonic
#        return HttpResponse('Success')
#    else:
#        return HttpResponse('Fail')
