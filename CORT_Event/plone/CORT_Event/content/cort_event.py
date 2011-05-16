"""Definition of the CORT_Event content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from plone.CORT_Event import CORT_EventMessageFactory as _
from plone.CORT_Event.interfaces import ICORT_Event
from plone.CORT_Event.config import PROJECTNAME

# Import from MPLPEvent - old style Plone product

from Products.CMFCore.utils import getToolByName
from Products.PortalTransforms import *
from Products.PortalTransforms.utils import TransformException
from Products.Archetypes.public import *

# PloneExFile imports
from Products.AttachmentField.AttachmentField import AttachmentField
from Products.AttachmentField.AttachmentWidget import AttachmentWidget

from Products.PloneExFile.interfaces import IExFile
from Products.PloneExFile.config import PROJECTNAME
from Products.PloneExFile import Permissions

#from Products.MPLPEvent.config import PROJECTNAME
import string

# End import from MPLPEvent

CORT_EventSchema = folder.ATFolderSchema.copy() + atapi.Schema((

#    StringField('title',
#            required=1,
#            searchable=1,
#            widget=StringWidget(),
#            ),
    TextField('description',
            required=1,
            searchable=1,
            widget=RichWidget(label='Description'),
            ),
#StringField('event_type',
#              required=1,
#              vocabulary=['Task Force Meeting', 'MPLP Training', 'Other Training', 'Other Event'],
#              searchable=0,
#              default="None",
#              widget=SelectionWidget(format='select', label='Event Type',
#                                     visible={'edit':'visible', 'view':'visible'}),
#             ),
    StringField('event_type',
            required=1,
            vocabulary='getCategories',
            searchable=0,
            default="None",
            index='FieldIndex',
            widget=SelectionWidget(format='select', label='Training Category', visible={'edit':'visible', 'view':'visible'}),
            ),
    LinesField('interest_areas',
            required=1,
            vocabulary='getInterestAreas',
            searchable=0,
            default="None",
            index="FieldIndex",
            widget=MultiSelectionWidget(format='select', label='Interest Areas', description='To select multiple rows, hold down Ctrl on your keyboard and click with your mouse.',),
            ),
    StringField('event_location',
            required=1,
            vocabulary='getLocations',
            searchable=0,
            default="None",
            index='FieldIndex',
            widget=SelectionWidget(format='select', label='Training Location', visible={'edit':'visible', 'view':'visible'}),
            ),
    StringField('registration',
            required=0,
            searchable=0,
            validators=("isURL"),
            widget=StringWidget(label='Link to Online Registration Form'),
            ),
    AttachmentField('registration_file',
            primary=1,
            searchable=1,
            required=0,
            languageIndependent=1,
            widget=AttachmentWidget(
                label="Registration File",
                label_msgid="label_file",
                description="Select the file to be added by clicking the 'Browse' button.",
                description_msgid="help_file",
                i18n_domain="plone",
                show_content_type=0,
                ),
            ),
#FileField('attachment',
#            searchable=0,
#            storage=ObjectManagedStorage(),
#           ),
    StringField('information',
            required=0,
            searchable=0,
            validators=("isURL"),
            widget=StringWidget(label='Link to External Information'),
            ),
#  LinesField('topics',
#              required=1,
#              searchable=0,
#              mutator='editTopics',
#              widget=LinesWidget(label='Topics',
#                                 macro='topic_chooser_widget',
#                                 helper_js=('popUpWindow.js',),),
#              index='KeywordIndex:schema'
#              ),
  #DateTimeField('start_datetime',
    DateTimeField('start',
            widget=CalendarWidget(label='Starting Date and Time'),
            ),
  #DateTimeField('end_datetime',
    DateTimeField('end',
            widget=CalendarWidget(label='Ending Date and Time'),
            ),
#BooleanField('front_page',
#          required=1,
#          default=0,
#          index='FieldIndex',
#          widget=BooleanWidget(label='Appears on the front page?',
#                               visible={'edit':'visible', 'view':'invisible'}),
#         ),
))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

CORT_EventSchema['title'].storage = atapi.AnnotationStorage()
CORT_EventSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    CORT_EventSchema,
    folderish=True,
    moveDiscussion=False
)

class CORT_Event(folder.ATFolder):
    """Description of the Example Type"""
    implements(ICORT_Event)

    meta_type = "CORT_Event"
    schema = CORT_EventSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    def getCategories(self):
        """Select Event Category"""
        return self.CORT_Event_Categories_List_Script()
    def getInterestAreas(self):
        """Select Event Interest Areas"""
        return self.CORT_Event_Interest_Areas_List_Script()
    def getLocations(self):
        """Select Event Location"""
        return self.CORT_Event_Locations_List_Script()
    
atapi.registerType(CORT_Event, PROJECTNAME)
