from django_mongodb_engine.storage import GridFSStorage

gridfs = GridFSStorage()
uploads = GridFSStorage(location='/uploads')

'''
class Better(models.Model):
    blob = GridFSField()
'''

'''
to retrival file from mangodb

>>> doc = Better()

GridFSField takes file-likes (and strings)...
>>> doc.blob = file_like
>>> doc.save()

 ... and always returns GridOuts.
>>> samedoc = Better.objects.get(...)
>>> samedoc.blob
<GridOut object at 0xfoobar>
'''