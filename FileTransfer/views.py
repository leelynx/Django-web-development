from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from FileTransfer.forms import NameForm
from FileTransfer.models import FileUpload

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            filename = form.cleaned_data['filename']
            filetransfer = FileUpload()
            filetransfer.username = username
            filetransfer.filepath = filename
            filetransfer.save()
            
            return  HttpResponse('File upload sucess')
    else:
        form = NameForm()
    return render_to_response('upload.html', {'form': form}, context_instance=RequestContext(request))
            
