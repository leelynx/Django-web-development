from django.db import models

class StorageMd5(models.Model):
    filename = models.CharField(max_length=200)
    md5num = models.CharField(max_length=40)
    def __unicode__(self):
        return "%s %s" % (self.filename, self.md5num)
    