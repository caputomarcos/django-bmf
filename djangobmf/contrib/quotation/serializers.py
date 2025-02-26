#!/usr/bin/python
# ex:set fileencoding=utf-8:

from __future__ import unicode_literals

from djangobmf.serializers import ModuleSerializer

from rest_framework import serializers


class QuotationSerializer(ModuleSerializer):
    state_name = serializers.ReadOnlyField(source='state.name')
    project_name = serializers.ReadOnlyField(source='project.name')

    class Meta:
        fields = (
            'quotation_number',
            'state',
            'state_name',
            'project',
            'project_name',
            'bmfdetail',
        )
