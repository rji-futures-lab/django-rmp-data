"""
Customized Django model field subclasses
"""
from django.db import models
from django.db.models import fields


class CopyFromFieldMixin(fields.Field):
    """
    Mixin to add attrs related to COPY FROM command to model fields.
    """
    def __init__(self, *args, **kwargs):
        self.source_column = kwargs.pop('source_column', None)
        super().__init__(*args, **kwargs)

    @property
    def copy_from_name(self):
        """
        Return the name of field to use in COPY FROM command.
        """
        return self.source_column or self.name
    

class CopyFromBooleanField(fields.BooleanField, CopyFromFieldMixin):
    """
    BooleanField subclass with attrs related to COPY FROM command.
    """
    pass


class CopyFromCharField(fields.CharField, CopyFromFieldMixin):
    """
    CharField subclass with attrs related to COPY FROM command.
    """
    pass


class CopyFromDateTimeField(fields.DateTimeField, CopyFromFieldMixin):
    """
    DateTimeField subclass with attrs related to COPY FROM command.
    """
    pass


class CopyFromDecimalField(fields.DecimalField, CopyFromFieldMixin):
    """
    DecimalField subclass with attrs related to COPY FROM command.
    """
    pass


class CopyFromIntegerField(fields.IntegerField, CopyFromFieldMixin):
    """
    IntegerField subclass with attrs related to COPY FROM command.
    """
    pass


class CopyFromDateTimeField(fields.DateTimeField, CopyFromFieldMixin):
    """
    DateTimeField subclass with attrs related to COPY FROM command.
    """
    pass


class CopyFromTextField(fields.TextField, CopyFromFieldMixin):
    """
    TextField subclass with attrs related to COPY FROM command.
    """
    pass


class CopyFromForeignKey(models.ForeignKey, CopyFromFieldMixin):
    """
    ForeignKey subclass with attrs related to COPY FROM command.
    """
    pass
