from zope.interface import Interface


class IAdapter(Interface):
    """Base interface for adapters"""

    def catalog():  # pragma: no cover
        """Returns portal_catalog"""

    def context_path():  # pragma: no cover
        """Path of the context"""

    def get_brains(interfaces=None, **query):  # pragma: no cover
        """Get brains."""

    def get_brain(interfaces=None, **query):  # pragma: no cover
        """Get brain which is supposed to be only one."""

    def get_object(interfaces=None, **query):  # pragma: no cover
        """Get object which is supposed to be only one."""

    def get_content_listing(interfaces=None, **query):  # pragma: no cover
        """Get ContentListing from brains gotten from get_brains method."""

    def getSessionData(create=True):  # pragma: no cover
        """getSessionData method from session_data_manager"""

    def event_datetime(item):  # pragma: no cover
        """Returns ulocalized_time event datetime."""

    def portal():  # pragma: no cover
        """Portal object"""

    def portal_path():  # pragma: no cover
        """Path of the portal"""
