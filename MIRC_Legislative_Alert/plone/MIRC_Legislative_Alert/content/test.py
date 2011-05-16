"""Definition of the MIRC_Legislative_Alerts content type"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from plone.MIRC_Legislative_Alerts import MIRC_Legislative_AlertsMessageFactory as _
from plone.MIRC_Legislative_Alerts.interfaces import IMIRC_Legislative_Alerts
from plone.MIRC_Legislative_Alerts.config import PROJECTNAME

# Imported from MPLPIssue.py - old style Plone prodcut 

from Products.Archetypes.public import *

# End of Import #

MIRC_Legislative_AlertsSchema = folder.ATFolderSchema.copy() + atapi.Schema((
    LinesField('interest_areas',
        required=0,
        searchable=0,
        vocabulary=['Employment', 'Immigration & Citizenship Status', "Driver's License & State ID Cards", 'Health', 'Education'],
        default="None",
        index="FieldIndex",
        widget=MultiSelectionWidget(format='select', label='Interest Areas', description='To select multiple rows, hold down Ctrl on your keyboard and click with your mouse.',),
        ),
    TextField('issue_summary',
        required=0,
        searchable=1,
        default_output_type='text/html',
        default_content_type='text/html',
        widget=RichWidget(label='Description'),
        ),
    TextField('contact',
        default_method='ContactMIRC',
        required=0,
        searchable=0,
        default_output_type='text/html',
        default_content_type='text/html',
        widget=RichWidget(label='Contact'),
        ),
    DateTimeField('issue_date',
        required=0,
        widget=CalendarWidget(label='Issue Date'),
        index='DateIndex'
        ),
    TextField('primary_sponsor',
        required=0,
        searchable=1,
        default_output_type='text/html',
        default_content_type='text/html',
        widget=RichWidget(label='Primary Sponnsor'),
        ),
    TextField('other_sponsors',
        required=0,
        searchable=1,
        default_output_type='text/html',
        default_content_type='text/html',
        widget=RichWidget(label='Other Sponsors'),
        ),
    TextField('status',
        required=0,
        searchable=1,
        default_output_type='text/html',
        default_content_type='text/html',
        widget=RichWidget(label='Status'),
        ),
    TextField('summary',
        required=0,
        searchable=1,
        default_output_type='text/html',
        default_content_type='text/html',
        widget=RichWidget(label='Summary'),
        ),
    ), marshall=PrimaryFieldMarshaller()
    # -*- Your Archetypes field definitions here ... -*-
)

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

MIRC_Legislative_AlertsSchema['title'].storage = atapi.AnnotationStorage()
MIRC_Legislative_AlertsSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(MIRC_Legislative_AlertsSchema, folderish=True,  moveDiscussion=False)

class MIRC_Legislative_Alerts(folder.ATFolder):
    """"""
    implements(IMIRC_Legislative_Alerts)

    meta_type = "MIRC_Legislative_Alerts"
    schema = MIRC_Legislative_AlertsSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    def ContactMIRC(self):
       """Returns the text of 'ContactMIRCText' in the custom skin"""
       return self.ContactMIRCText.data
 
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(MIRC_Legislative_Alerts, PROJECTNAME)
?