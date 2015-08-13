#encoding=utf8
from django.conf import settings

class Mydb(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'booksapp':
            return 'books'
        elif model._meta.app_label == 'calcmd5_app':
            return 'md5_storage'
        else:
            return 'default' 
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'booksapp':
            return 'books'
        elif model._meta.app_label == 'calcmd5_app':
            return 'md5_storage'
        else:
            return 'default' 
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'booksapp' or obj2._meta.app_label == 'calcmd5_app':
            return True

    def allow_syncdb(self, db, model):
        if db == 'books':
            return model._meta.app_label == 'booksapp'
        elif db == 'md5_storage':
            return model._meta.app_label == 'calcmd5_app'
        return None