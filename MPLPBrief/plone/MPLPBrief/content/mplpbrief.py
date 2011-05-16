"""Definition of the MPLPBrief content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from plone.MPLPBrief import MPLPBriefMessageFactory as _
from plone.MPLPBrief.interfaces import IMPLPBrief
from plone.MPLPBrief.config import PROJECTNAME

from Products.CMFCore.utils import getToolByName
from Products.PortalTransforms import *
from Products.PortalTransforms.utils import TransformException
from Products.Archetypes.public import *
#from Products.MPLPBrief.config import PROJECTNAME
import string

MPLPBriefSchema = folder.ATFolderSchema.copy() + atapi.Schema((

  StringField('title',
              required=1,
              searchable=1,
              widget=StringWidget(label='Case Name'),
             ),
  TextField('abstract',
            required=0,
            searchable=1,
            widget=RichWidget(label='Abstract'),
           ),
  StringField('document_type',
              required=1,
              vocabulary=['Brief', 'Motion', 'Cover Letter', 'Other'],
              searchable=0,
              widget=SelectionWidget(label='Document Type', format='select'),
             ),
  TextField('advocate_names',
             required=0,
             searchable=1,
             widget=TextAreaWidget(label='Advocate name(s)'),
              ),
  TextField('program',
             required=0,
             searchable=1,
             widget=TextAreaWidget(label='Program and Branch'),
           ),
  TextField('persons',
             required=0,
             searchable=1,
             widget=TextAreaWidget(label='Persons represented'),
              ),
  StringField('forum',
              required=0,
              searchable=1,
              widget=StringWidget(label='Forum'),
             ),

  LinesField('keywords',
              required=0,
              searchable=1,
              widget=LinesWidget(label='Keywords'),
             ),
  LinesField('topics',
              required=1,
              searchable=0,
              mutator='editTopics',
              widget=LinesWidget(label='Topics',
                                 macro='topic_chooser_widget',
                                 helper_js=('popUpWindow.js',),),
              index='KeywordIndex:schema'
              ),
  DateTimeField('date_filed',
                widget=CalendarWidget(label='Date filed', visible={'view': 'visible', 'edit':'visible'}),
               ),
  FileField('file0',
            searchable=0,
            storage=ObjectManagedStorage(),
            widget=FileWidget(label='Related document'),
           ),
  FileField('file1',
            searchable=0,
            storage=ObjectManagedStorage(),
            widget=FileWidget(label='Related document'),
           ),
  FileField('file2',
            searchable=0,
            storage=ObjectManagedStorage(),
            widget=FileWidget(label='Related document'),
           ),
  FileField('file3',
            searchable=0,
            storage=ObjectManagedStorage(),
            widget=FileWidget(label='Related document'),
           ),
  FileField('file4',
            searchable=0,
            storage=ObjectManagedStorage(),
            widget=FileWidget(label='Related document'),
           ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

MPLPBriefSchema['title'].storage = atapi.AnnotationStorage()
MPLPBriefSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    MPLPBriefSchema,
    folderish=True,
    moveDiscussion=False
)

class MPLPBrief(folder.ATFolder):
    """Description of the Example Type"""
    implements(IMPLPBrief)

    meta_type = "MPLPBrief"
    schema = MPLPBriefSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    def txng_get(self, attr='SearchableText'):
        """Special searchable text source for TextIndexNG2"""

        if attr[0] != 'SearchableText':
            return

        index_source = ''
        encoding = 'utf-8'
        mimetype = 'text/plain'

        # Get the searchable text

        index_source = self.SearchableText()

        # Get the file and convert it and add its text
        # to 'index_source'

        pt = getToolByName(self, 'portal_transforms')

        # Here you have to change the accessor method to your
        # specific needs: I access the field 'file0'

        f = self.getFile0()
        if f:
            mt = f.getContentType()

        try:
            result = pt.convertTo('text/plain', str(f), mimetype=mt ).getData()
        except TransformException:
            result = ''

            index_source += result

        return (index_source, mimetype, encoding)

        def editTopics(self, value):
            """Massage the topics string"""

            index = self.ClientLibraryIndex.Index

            # Find the topics and their parents for this document
            #
            # Note: topics is a list that looks like: ['12345 (title1)', '67890 (title2)']
            #
            # We need to get rid of the title part


            topics=value
            topics_stripped=[]

            for t in topics:
                topic = string.split(t)[0]
                topics_stripped.append(topic)

            # Call the orignal mutator

        self.getField('topics').set(self, topics_stripped)
    
atapi.registerType(MPLPBrief, PROJECTNAME)
