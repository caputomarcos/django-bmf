#!/usr/bin/python
# ex:set fileencoding=utf-8:

from __future__ import unicode_literals

"""
overwrites bmf settings from django's settings
"""

from django.conf import settings as djsettings


class Settings(object):
    """
    This objects holds all settings used from djangobmf. is presents
    the values as propertiers, which is neccecary for testing
    with variable settings
    """

    ACTIVITY_WORKFLOW = "glyphicon-random"
    ACTIVITY_COMMENT = "glyphicon-comment"
    ACTIVITY_UPDATED = "glyphicon-pencil"
    ACTIVITY_FILE = "glyphicon-paperclip"
    ACTIVITY_CREATED = "glyphicon-file"
    ACTIVITY_UNKNOWN = "glyphicon-question-sign"

    @property
    def APP_LABEL(self):  # noqa
        return getattr(djsettings, 'BMF_APP_LABEL', 'djangobmf')

    @property
    def USE_CELERY(self):  # noqa
        return getattr(djsettings, 'BMF_USE_CELERY', False)

    @property
    def CACHE_DEFAULT_CONNECTION(self):  # noqa
        return getattr(djsettings, 'BMF_CACHE_DEFAULT_CONNECTION', 'default')

    @property
    def CONTRIB_ACCOUNT(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_ACCOUNT'):
            setattr(djsettings, 'BMF_CONTRIB_ACCOUNT', 'djangobmf_accounting.Account')
        return getattr(djsettings, 'BMF_CONTRIB_ACCOUNT')

    @property
    def CONTRIB_ADDRESS(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_ADDRESS'):
            setattr(djsettings, 'BMF_CONTRIB_ADDRESS', 'djangobmf_address.Address')
        return getattr(djsettings, 'BMF_CONTRIB_ADDRESS')

    @property
    def CONTRIB_CUSTOMER(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_CUSTOMER'):
            setattr(djsettings, 'BMF_CONTRIB_CUSTOMER', 'djangobmf_customer.Customer')
        return getattr(djsettings, 'BMF_CONTRIB_CUSTOMER')

    @property
    def CONTRIB_EMPLOYEE(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_EMPLOYEE'):
            setattr(djsettings, 'BMF_CONTRIB_EMPLOYEE', 'djangobmf_employee.Employee')
        return getattr(djsettings, 'BMF_CONTRIB_EMPLOYEE')

    @property
    def CONTRIB_GOAL(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_GOAL'):
            setattr(djsettings, 'BMF_CONTRIB_GOAL', 'djangobmf_task.Goal')
        return getattr(djsettings, 'BMF_CONTRIB_GOAL')

    @property
    def CONTRIB_INVOICE(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_INVOICE'):
            setattr(djsettings, 'BMF_CONTRIB_INVOICE', 'djangobmf_invoice.Invoice')
        return getattr(djsettings, 'BMF_CONTRIB_INVOICE')

    @property
    def CONTRIB_TAX(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_TAX'):
            setattr(djsettings, 'BMF_CONTRIB_TAX', 'djangobmf_taxing.Tax')
        return getattr(djsettings, 'BMF_CONTRIB_TAX')

    @property
    def CONTRIB_TASK(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_TASK'):
            setattr(djsettings, 'BMF_CONTRIB_TASK', 'djangobmf_task.Task')
        return getattr(djsettings, 'BMF_CONTRIB_TASK')

    @property
    def CONTRIB_TEAM(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_TEAM'):
            setattr(djsettings, 'BMF_CONTRIB_TEAM', 'djangobmf_team.Team')
        return getattr(djsettings, 'BMF_CONTRIB_TEAM')

    @property
    def CONTRIB_POSITION(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_POSITION'):
            setattr(djsettings, 'BMF_CONTRIB_POSITION', 'djangobmf_position.Position')
        return getattr(djsettings, 'BMF_CONTRIB_POSITION')

    @property
    def CONTRIB_PRODUCT(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_PRODUCT'):
            setattr(djsettings, 'BMF_CONTRIB_PRODUCT', 'djangobmf_product.Product')
        return getattr(djsettings, 'BMF_CONTRIB_PRODUCT')

    @property
    def CONTRIB_PROJECT(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_PROJECT'):
            setattr(djsettings, 'BMF_CONTRIB_PROJECT', 'djangobmf_project.Project')
        return getattr(djsettings, 'BMF_CONTRIB_PROJECT')

    @property
    def CONTRIB_QUOTATION(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_QUOTATION'):
            setattr(djsettings, 'BMF_CONTRIB_QUOTATION', 'djangobmf_quotation.Quotation')
        return getattr(djsettings, 'BMF_CONTRIB_QUOTATION')

    @property
    def CONTRIB_TIMESHEET(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_TIMESHEET'):
            setattr(djsettings, 'BMF_CONTRIB_TIMESHEET', 'djangobmf_timesheet.Timesheet')
        return getattr(djsettings, 'BMF_CONTRIB_TIMESHEET')

    @property
    def CONTRIB_TRANSACTION(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_TRANSACTION'):
            setattr(djsettings, 'BMF_CONTRIB_TRANSACTION', 'djangobmf_accounting.Transaction')
        return getattr(djsettings, 'BMF_CONTRIB_TRANSACTION')

    @property
    def CONTRIB_TRANSACTIONITEM(self):  # noqa
        if not hasattr(djsettings, 'BMF_CONTRIB_TRANSACTIONITEM'):
            setattr(djsettings, 'BMF_CONTRIB_TRANSACTIONITEM', 'djangobmf_accounting.TransactionItem')
        return getattr(djsettings, 'BMF_CONTRIB_TRANSACTIONITEM')

    @property
    def REPORTING_SERVER(self):  # noqa
        return getattr(djsettings, 'BMF_REPORTING_SERVER', None)

    @property
    def DEFAULT_CURRENCY(self):  # noqa
        return getattr(djsettings, 'BMF_DEFAULT_CURRENCY', 'EUR')


settings = Settings()
