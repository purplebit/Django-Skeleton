from django.db import models
from django.db.models.query import QuerySet

class DeleteStatusManager(models.Manager):
    """
    Manager that marks objects as deleted instead of actually deleting them.

    Expects to be used with a model with an ``is_deleted`` boolean field.

    Doesn't hide deleted objects from ``all()``, but instead gives an easy way
    to filter them in/out (``deleted()``/``active()``). Also overrides
    ``delete()`` to mark deleted in bulk.
    """

    def get_query_set(self):
        return DeleteStatusQuerySet(self.model, using=self._db)

    def active(self):
        """
        Return only objects that haven't been deleted.
        """
        return self.get_query_set().active()

    def deleted(self):
        """
        Return only objects that have been deleted.
        """
        return self.get_query_set().deleted()


class DeleteStatusQuerySet(QuerySet):
    """
    QuerySet to manage objects with ``is_deleted`` flags.

    See DeleteStatusManager for more details.
    """
    def active(self):
        """
        Return only objects that haven't been deleted.
        """
        return self.filter(is_deleted=False)

    def deleted(self):
        """
        Return only objects that have been deleted.
        """
        return self.filter(is_deleted=True)

    def delete(self):
        """
        Mark records in the current QuerySet as deleted.
        """
        self.update(is_deleted=True)
