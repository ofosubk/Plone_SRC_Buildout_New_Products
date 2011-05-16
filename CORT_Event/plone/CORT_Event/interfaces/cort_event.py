from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from plone.CORT_Event import CORT_EventMessageFactory as _

class ICORT_Event(Interface):
    """Description of the Example Type"""
    
    # -*- schema definition goes here -*-
