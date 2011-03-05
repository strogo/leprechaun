from django.conf import settings


GRIDFS_HOST = getattr(settings, 'LEPRECHAUN_GRIDFS_HOST', 'localhost') # or list ['host a', 'host b']
GRIDFS_PORT = getattr(settings, 'LEPRECHAUN_GRIDFS_PORT', 27017)
GRIDFS_DATABASE_NAME = getattr(settings, 'LEPRECHAUN_GRIDFS_DATABASE_NAME', u'gridfs_storage')


