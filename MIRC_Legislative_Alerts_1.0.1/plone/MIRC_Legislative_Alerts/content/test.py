from Products.Archetypes.public import *
from Products.MPLPIssue.config import PROJECTNAME

schema = BaseSchema + Schema((
StringField('submitted_by',
  #schemata="Page One",
   required=1,
   searchable=0,
   default_method='memberFullname',
   widget=StringWidget(),
    ),
LinesField('interest_areas',
  #schemata="Page One",
              required=1,
              vocabulary='interestAreas',
              searchable=0,
              default="None",
              index="FieldIndex",
              widget=MultiSelectionWidget(format='select', label='Interest Areas', description='To select multiple rows, hold down Ctrl on your keyboard and click with your mouse.',),
             ),
TextField('program_area',
  #schemata="Page One",
   required=0,
   searchable=1,
         default_output_type='text/html',
         default_content_type='text/html',
   widget=StringWidget(),
    ),
TextField('issue_summary',
  #schemata="Page One",
   required=1,
   searchable=1,
         default_output_type='text/html',
         default_content_type='text/html',
   widget=TextAreaWidget(label='Summary'),
    ),
TextField('persons_affected',
  #schemata="Page One",
   required=0,
   searchable=0,
         default_output_type='text/html',
         default_content_type='text/html',
   widget=TextAreaWidget(label='Persons Affected'),
    ),
TextField('contact',
  #schemata="Page One",
   required=0,
   searchable=0,
         default_output_type='text/html',
         default_content_type='text/html',
   widget=TextAreaWidget(label='Contact'),
    ),
DateTimeField('issue_date',
  #schemata="Page One",
              required=1,
              widget=CalendarWidget(label='Issue Date'),
              index='DateIndex'
             ),
TextField('background',
  #schemata="Page One",
   required=0,
   searchable=1,
         default_output_type='text/html',
         default_content_type='text/html',
   widget=RichWidget(label='Background'),
    ),
TextField('whats_happening',
  #schemata="Page Two",
   required=0,
   searchable=1,
         default_output_type='text/html',
         default_content_type='text/html',
   widget=RichWidget(label='What is happening?'),
    ),
#TextField('remaining_body',
   #required=0,
   #searchable=1,
         #default_output_type='text/html',
         #default_content_type='text/html',
   #widget=TextAreaWidget(label='The remaining body'),
    #),
TextField('advocates_do',
  #schemata="Page Two",
   required=0,
   searchable=0,
         default_output_type='text/html',
         default_content_type='text/html',
   widget=RichWidget(label='What do advocates do?'),
    ),
TextField('clients_do',
  #schemata="Page Two",
   required=0,
   searchable=0,
         default_output_type='text/html',
         default_content_type='text/html',
   widget=RichWidget(label='What do clients do?'),
    ),
TextField('find_help',
  #schemata="Page Two",
         default_method='FindingHelp',
   required=0,
   searchable=0,
         default_output_type='text/html',
         default_content_type='text/html',
   widget=RichWidget(label='Finding help'),
    ),
ReferenceField('appears_in_newsletter',
         required=0,
         searchable=0,
         multiValued=True,
         relationship="appearsInNewsletters",
         allowed_types="MPLPNewsletter",
         widget=ReferenceWidget(label='Appears in these newsletters',
                               visible={'edit':'visible', 'view':'invisible'}),
          ),

))


class MPLPIssue(BaseContent):
  """A MPLP Issue Alert archetype"""

  schema = schema
  actions = (
                { 'id': 'view',
                  'name': 'View',
                  'action': 'string:${object_url}/MPLPIssueAlert_view',
                  'category':'object',
                  },
      )



  def FindingHelp(self):
    """Returns the text of 'FindingHelpText' in the custom skin"""
    return self.FindingHelpText.data

  def interestAreas(self):
    """Select list of interest areas"""
    return self.interestAreasList()

  def memberFullname(self):
    """Get logged in users full name"""
    member = self.portal_membership.getAuthenticatedMember()
    return getattr(member, 'fullname', '')

registerType(MPLPIssue, PROJECTNAME)
?