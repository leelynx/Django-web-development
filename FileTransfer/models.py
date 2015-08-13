from django.db import models

class FileUpload(models.Model):
    username = models.CharField(max_length = 30)
    filepath = models.FileField(upload_to= './FileTransfer/upload')
    
    def __unicode__(self):
        return self.username
    