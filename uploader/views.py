from django.views.generic import TemplateView
from csv_uploader.settings import MEDIA_ROOT, BASE_DIR
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from . import tasks

class UploaderView(TemplateView):
    '''
    View to handle file upload
    '''

    template_name = 'index.html'

    def post(self, request):
        file_c = request.FILES['uploadedfile']
        fs = FileSystemStorage()
        filename = fs.save(file_c.name, file_c)
        uploaded_file_url = fs.url(filename)
        tasks.process.delay(BASE_DIR+uploaded_file_url)
        return HttpResponse('Uploaded')


