import datetime
from django.db import models
from . import managers
from django.utils.timezone import now as utcnow
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class TimestampedModel(models.Model):
    """
    Abstract base model that keeps track of added/updated timestamps.
    """
    added = models.DateTimeField(default=utcnow, db_index=True)
    updated = models.DateTimeField(default=utcnow, db_index=True)

    class Meta(object):
        abstract = True

    def save(self, *args, **kwargs):
        self.updated = utcnow()
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

class GenericLinkedModel(models.Model):
    """
    Abstract base model that allows for an object to be linked (foreign-keyed)
    to various models. Useful example: Comments or tags for different types of
    objects.

    Example Usage:
    ==============
    
    from django.contrib.contenttypes import generic
    ...

    class Comment(GenericLinkedModel):
        text = models.Charfield(max_length=500)
        ...

    class Post(models.Model):
        comments = generic.GenericRelation(Comment)
        ...

    """

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True
