Introduction
============

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.
We use PloneTestCase to set up this test as well, so we have a full Plone site
to play with. We *can* inspect the state of the portal, e.g. using 
self.portal and self.folder, but it is often frowned upon since you are not
treating the system as a black box. Also, if you, for example, log in or set
roles using calls like self.setRoles(), these are not reflected in the test
browser, which runs as a separate session.

Being a doctest, we can tell a story here.

First, we must perform some setup. We use the testbrowser that is shipped
with Five, as this provides proper Zope 2 integration. Most of the 
documentation, though, is in the underlying zope.testbrower package.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> self.portal.error_log._ignored_exceptions = ()

With that in place, we can go to the portal front page and log in. We will
do this using the default user from PloneTestCase:

    >>> from Products.PloneTestCase.setup import portal_owner, default_password

    >>> browser.open(portal_url)

We have the login portlet, so let's use that.

    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Here, we set the value of the fields on the login form and then simulate a
submit click.

We then test that we are still on the portal front page:

    >>> browser.url == portal_url
    True

And we ensure that we get the friendly logged-in message:

    >>> "You are now logged in" in browser.contents
    True


-*- extra stuff goes here -*-
The MFPP_Library_Resource content type
===============================

In this section we are tesing the MFPP_Library_Resource content type by performing
basic operations like adding, updadating and deleting MFPP_Library_Resource content
items.

Adding a new MFPP_Library_Resource content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'MFPP_Library_Resource' and click the 'Add' button to get to the add form.

    >>> browser.getControl('MFPP_Library_Resource').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'MFPP_Library_Resource' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'MFPP_Library_Resource Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'MFPP_Library_Resource' content item to the portal.

Updating an existing MFPP_Library_Resource content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New MFPP_Library_Resource Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New MFPP_Library_Resource Sample' in browser.contents
    True

Removing a/an MFPP_Library_Resource content item
--------------------------------

If we go to the home page, we can see a tab with the 'New MFPP_Library_Resource
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New MFPP_Library_Resource Sample' in browser.contents
    True

Now we are going to delete the 'New MFPP_Library_Resource Sample' object. First we
go to the contents tab and select the 'New MFPP_Library_Resource Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New MFPP_Library_Resource Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New MFPP_Library_Resource
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New MFPP_Library_Resource Sample' in browser.contents
    False

Adding a new MFPP_Library_Resource content item as contributor
------------------------------------------------

Not only site managers are allowed to add MFPP_Library_Resource content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'MFPP_Library_Resource' and click the 'Add' button to get to the add form.

    >>> browser.getControl('MFPP_Library_Resource').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'MFPP_Library_Resource' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'MFPP_Library_Resource Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new MFPP_Library_Resource content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)



