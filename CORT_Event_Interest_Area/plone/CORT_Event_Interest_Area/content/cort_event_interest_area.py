"""Definition of the CORT_Event_Interest_Area content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from plone.CORT_Event_Interest_Area import CORT_Event_Interest_AreaMessageFactory as _
from plone.CORT_Event_Interest_Area.interfaces import ICORT_Event_Interest_Area
from plone.CORT_Event_Interest_Area.config import PROJECTNAME

# Import from MPLPInterest.py - old style Plone product
from Products.CMFCore.utils import getToolByName
from Products.PortalTransforms import *
from Products.PortalTransforms.utils import TransformException
from Products.Archetypes.public import *
import string
# End of import from MPLPInterest.py

CORT_Event_Interest_AreaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

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
#    StringField('directions',
#            required=0,
#            searchable=0,
#            validators=("isURL"),
#            widget=StringWidget(label='Link to Directions'),
#            ),
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

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

CORT_Event_Interest_AreaSchema['title'].storage = atapi.AnnotationStorage()
CORT_Event_Interest_AreaSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    CORT_Event_Interest_AreaSchema,
    folderish=True,
    moveDiscussion=False
)

class CORT_Event_Interest_Area(folder.ATFolder):
    """Description of the Example Type"""
    implements(ICORT_Event_Interest_Area)

    meta_type = "CORT_Event_Interest_Area"
    schema = CORT_Event_Interest_AreaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(CORT_Event_Interest_Area, PROJECTNAME)
