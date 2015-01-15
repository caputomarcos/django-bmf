#!/usr/bin/python
# ex:set fileencoding=utf-8:
# flake8: noqa
# pragma: no cover

from __future__ import unicode_literals

from .models import Employee
from djangobmf.utils.testcases import BaseTestCase
from djangobmf.utils.testcases import ModuleMixin

class TaxTests(ModuleMixin, BaseTestCase):

    def test_urls_user(self):
        """
        """
        self.model = Employee

        data = self.autotest_ajax_get('create', kwargs={'key': 'default'})
        data = self.autotest_ajax_post('create', kwargs={'key': 'default'}, data={
            'name': 'test',
            'email': 'testing@django-bmf.org',
        })
        self.assertNotEqual(data["object_pk"], 0)
#       self.autotest_get('index', 200)

        obj = self.get_latest_object()
        a = '%s'%obj # check if object name has any errors

        self.autotest_get('detail', kwargs={'pk': obj.pk}, api=False)
        data = self.autotest_ajax_get('update', kwargs={'pk': obj.pk})
        self.autotest_get('delete', kwargs={'pk': obj.pk})
        self.autotest_post('delete', status_code=302, kwargs={'pk': obj.pk})
