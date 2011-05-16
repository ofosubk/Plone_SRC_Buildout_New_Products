"""Definition of the CORT_Event_Category content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from plone.CORT_Event_Category import CORT_Event_CategoryMessageFactory as _
from plone.CORT_Event_Category.interfaces import ICORT_Event_Category
from plone.CORT_Event_Category.config import PROJECTNAME

# Import from MPLPInterest.py - old style Plone product

from Products.CMFCore.utils import getToolByName
from Products.PortalTransforms import *
from Products.PortalTransforms.utils import TransformException
from Products.Archetypes.public import *
#from Products.MPLPInterest.config import PROJECTNAME
import string

# End of import from MPLPInterest.py

CORT_Event_CategorySchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

#    StringField('title',
#        required=1,
#        searchable=1,
#        widget=StringWidget(),
#        ),
    TextField('description',
        required=1,
        searchable=1,
        widget=RichWidget(label='Description'),
        ),
#    TextField('body',
#        required=0,
#        searchable=1,
#        default_output_type='text/html',
#        widget=RichWidget(),
#        ),
#    TextField('info',
#        required=0,
#        searchable=1,
#        default_output_type='text/html',
#        widget=TextAreaWidget(label='Quick Reference Info'),
#        ),
#    ImageField('photo'),
#    TextField('other_news_info',
#        required=0,
#        searchable=1,
#        default_output_type='text/html',
#        widget=TextAreaWidget(label='Other News Information'),
#        ),
#    TextField('other_events_info',
#        required=0,
#        searchable=1,
#        default_output_type='text/html',
#        widget=TextAreaWidget(label='Other Events Information'),
#        ),
 #   TextField('other_resources_info',
 #       required=0,
 #       searchable=1,
 #       default_output_type='text/html',
 #       widget=TextAreaWidget(label='Other Resources Information'),
 #       ),
#    TextField('links',
#        required=0,
#        searchable=1,
#        default_output_type='text/html',
#        widget=RichWidget(label='Essential Links',),
#        ),
#    StringField('notification_email',
#        required=1,
#        widget=StringWidget(label='Notification Email', description='Provide an email address to notify when Issue Alerts are published.',),
#        ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CORT_Event_CategorySchema['title'].storage = atapi.AnnotationStorage()
CORT_Event_CategorySchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(CORT_Event_CategorySchema, moveDiscussion=False)

class CORT_Event_Category(base.ATCTContent):
    """Description of the Example Type"""
    implements(ICORT_Event_Category)

    meta_type = "CORT_Event_Category"
    schema = CORT_Event_CategorySchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(CORT_Event_Category, PROJECTNAME)
