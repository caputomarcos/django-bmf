#!/usr/bin/python
# ex:set fileencoding=utf-8:

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djangobmf.document.storage import BMFStorage

from djangobmf.utils.generate_filename import generate_filename


@python_2_unicode_compatible
class Document(models.Model):
    name = models.CharField(_('Name'), max_length=120, null=True, blank=True, editable=False)
    file = models.FileField(_('File'), upload_to=generate_filename, storage=BMFStorage())
    size = models.PositiveIntegerField(null=True, blank=True, editable=False)
    # mime = models.CharField(_('Mime-Type'), max_length=120, null=True, blank=True, editable=False)

    is_static = models.BooleanField(default=False)

    # this fields are added due to a soft dependency to customer and projects
    # because djangobmf can't relay on those models to be present!
    customer_pk = models.PositiveIntegerField(null=True, blank=True, editable=False, db_index=True)
    project_pk = models.PositiveIntegerField(null=True, blank=True, editable=False, db_index=True)

    content_type = models.ForeignKey(
        ContentType,
        related_name="bmf_document",
        null=True,
        blank=True,
        editable=False,
        on_delete=models.SET_NULL,
    )
    content_id = models.PositiveIntegerField(null=True, blank=True, editable=False)
    content_object = GenericForeignKey('content_type', 'content_id')

    modified = models.DateTimeField(_("Modified"), auto_now=True, editable=False, null=True, blank=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True, editable=False, null=True, blank=False)
    modified_by = models.ForeignKey(
        getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),
        null=True, blank=True, editable=False,
        related_name="+", on_delete=models.SET_NULL)
    created_by = models.ForeignKey(
        getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),
        null=True, blank=True, editable=False,
        related_name="+", on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
        get_latest_by = "modified"
        abstract = True

    def __str__(self):
        return self.name

    def clean(self):
        if self.file:
            self.size = self.file.size

        if not self.name:
            self.name = self.file.name.split(r'/')[-1]

        if hasattr(self, 'project') and hasattr(self.content_object, 'bmfget_project'):
            self.project_pk = getattr(self.content_object.bmfget_project(), 'pk', None)

        if hasattr(self, 'customer') and hasattr(self.content_object, 'bmfget_customer'):
            self.customer_pk = getattr(self.content_object.bmfget_customer(), 'pk', None)

    @models.permalink
    def bmffile_download(self):
        """
        A permalink to the default view of this model in the BMF-System
        """
        return ('djangobmf:document-get', (), {"pk": self.pk})
