import datetime
from django.db import models
from . import managers

class TimestampedModel(models.Model):
    """
    Abstract base model that keeps track of added/updated timestamps.
    """
    added = models.DateTimeField(default=datetime.datetime.now, db_index=True)
    updated = models.DateTimeField(default=datetime.datetime.now, db_index=True)

    class Meta(object):
        abstract = True

    def save(self, *args, **kwargs):
        self.updated = datetime.datetime.now()
        super(TimestampedModel, self).save(*args, **kwargs)

class DeleteStatusModel(models.Model):
    """
    Abstract base model that flags an object as deleted instead of actually
    deleting it.
    """
    is_deleted = models.BooleanField(default=False, db_index=True)
    objects = managers.DeleteStatusManager()

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        if kwargs.pop('really_delete', False):
            super(DeleteStatusModel, self).delete()
        else:
            self.is_deleted = True
            self.save()
