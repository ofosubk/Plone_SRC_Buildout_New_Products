"""Definition of the MLA_Organization content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from plone.MLA_Organization import MLA_OrganizationMessageFactory as _
from plone.MLA_Organization.interfaces import IMLA_Organization
from plone.MLA_Organization.config import PROJECTNAME

from Products.Archetypes.public import *
#from Products.Organization.config import PROJECTNAME
import string

MLA_OrganizationSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    StringField('programname',
        required=1,
        searchable=1,
        widget=StringWidget(description="""Program Name"""),
        ),
    StringField('address',
        required=1,
        searchable=0,
        widget=StringWidget(description="""Addresss"""),
        ),
    StringField('city',
        required=1,
        searchable=1,
        widget=StringWidget(description="""City"""),
        ),
    StringField('state',
        required=1,
        default="MI",
        searchable=0,
        widget=StringWidget(description="""State"""),
        ),
    StringField('zipcode',
        required=1,
        searchable=0,
        widget=StringWidget(description="""Zipcode"""),
        index='FieldIndex'
        ),
    StringField('sponsor_org',
        required=0,
        searchable=0,
        widget=StringWidget(description="""Sponsoring Organization"""),
        ),
    StringField('phone',
        required=1,
        searchable=0,
        widget=StringWidget(description="""Phone"""),
        ),
    StringField('fax',
        required=0,
        searchable=0,
        widget=StringWidget(description="""Fax"""),
        ),
    StringField('email',
        required=0,
        searchable=0,
        widget=StringWidget(description="""Email"""),
        ),
    StringField('url',
        required=0,
        searchable=0,
        widget=StringWidget(description="""URL"""),
        ),
    StringField('contact',
        required=0,
        searchable=0,
        widget=StringWidget(description="""Contact"""),
        ),
    BooleanField('legal_service',
        required=0,
        index='FieldIndex',
        ),
    BooleanField('statewide',
        required=0,
        default=0,
        index='FieldIndex',
        ),
    #LinesField('topics',
    #    required=0,
    #    searchable=0,
    #    mutator='editTopics',
    #        widget=LinesWidget(label='Topics',
    #        description='Index Topics',
    #        macro='topic_chooser_widget',
    #        helper_js=('popUpWindow.js',),),
    #        index='KeywordIndex:schema',
    #    ),
    LinesField('counties',
        required=0,
        searchable=0,
        widget=LinesWidget(label='Counties Server'),
        index='KeywordIndex:schema'
        ),
    TextField('screening',
        required=0,
        searchable=1,
        widget=TextAreaWidget(label='Screening'),
        ),
    TextField('eligibility',
        required=0,
        searchable=1,
        widget=TextAreaWidget(label='Eligibility'),
        ),
    TextField('legal_areas',
        required=0,
        searchable=1,
        widget=TextAreaWidget(label='Legal Areas'),
        ),
    TextField('services',
        required=0,
        searchable=1,
        widget=TextAreaWidget(label='Services'),
        ),
    TextField('notes',
        required=0,
        searchable=1,
        widget=TextAreaWidget(lable='Notes'),
        ),


))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

MLA_OrganizationSchema['title'].storage = atapi.AnnotationStorage()
MLA_OrganizationSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    MLA_OrganizationSchema,
    folderish=True,
    moveDiscussion=False
)

class MLA_Organization(folder.ATFolder):
    """Description of the Example Type"""
    implements(IMLA_Organization)

    meta_type = "MLA_Organization"
    schema = MLA_OrganizationSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(MLA_Organization, PROJECTNAME)
