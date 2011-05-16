"""Definition of the MFPP_Library_Resource content type
"""

 # ske imports #
 
from copy import deepcopy

# Zope imports
from AccessControl import ClassSecurityInfo
from ZODB.POSException import ConflictError

# CMF imports
from Products.CMFCore.permissions import View, ModifyPortalContent
from Products.CMFCore.utils import getToolByName

# Archetypes imports
from Products.Archetypes.utils import fixSchema
try:
    from Products.LinguaPlone.public import *
except ImportError:
    # No multilingual support
    from Products.Archetypes.public import *

# ATCT imports
from Products.ATContentTypes.content.base import ATCTFileContent
from Products.ATContentTypes.content.file import ATFileSchema, ATFile

# PloneExFile imports
from Products.AttachmentField.AttachmentField import AttachmentField
from Products.AttachmentField.AttachmentWidget import AttachmentWidget

from Products.PloneExFile.interfaces import IExFile
from Products.PloneExFile.config import PROJECTNAME
from Products.PloneExFile import Permissions

# ske imports end #

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from plone.MFPP_Library_Resource import MFPP_Library_ResourceMessageFactory as _
from plone.MFPP_Library_Resource.interfaces import IMFPP_Library_Resource
from plone.MFPP_Library_Resource.config import PROJECTNAME

MFPP_Library_ResourceSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((
    StringField('url',
        required=0,
        searchable=0,
        validators=("isURL"),
        widget=StringWidget(),
        ),
    AttachmentField('file',
        primary=True,
        searchable=True,
        required=False,
        languageIndependent=True,
        widget=AttachmentWidget(
            label="File",
            label_msgid="label_file",
            description="Select the file to be added by clicking the 'Browse' button.",
            description_msgid="help_file",
            i18n_domain="plone",
            show_content_type=False,
            ),
        ),
    LinesField('document_type',
        required=1,
        index="FieldIndex",
        default="New Advocate",
        vocabulary='DocumentTypes',
        searchable=0,
        widget=MultiSelectionWidget(format='select', label='Material Types', description='To select multiple rows, hold down Ctrl on your keyboard and click with your mouse.',),
        ),
    LinesField('topics',
        required=1,
        searchable=0,
        mutator='editTopics',
        widget=LinesWidget(label='Topics',
            macro='topic_chooser_widget',
            helper_js=('popUpWindow.js',),
            ),
        index='KeywordIndex:schema'
        ),
    DateTimeField('date_posted',
        required=1,
        widget=CalendarWidget(label='Date Posted',
        visible={'edit':'visible', 'view':'invisible'}),
        index='DateIndex:schema'
        ),
    ), marshall=PrimaryFieldMarshaller()
    # -*- Your Archetypes field definitions here ... -*-
)

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

MFPP_Library_ResourceSchema['title'].storage = atapi.AnnotationStorage()
MFPP_Library_ResourceSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(MFPP_Library_ResourceSchema, moveDiscussion=False)

class MFPP_Library_Resource(base.ATCTContent):
    """Michigan Foreclosure Prevention Project Library Resource Item"""
    implements(IMFPP_Library_Resource)

    meta_type = "MFPP_Library_Resource"
    schema = MFPP_Library_ResourceSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    def DocumentTypes(self):
        """Select Document Type"""
        return self.DocumentTypeList()
 
atapi.registerType(MFPP_Library_Resource, PROJECTNAME)
