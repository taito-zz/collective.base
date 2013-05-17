from collective.base.interfaces import IViewlet
from plone.app.layout.viewlets.common import ViewletBase
from zope.interface import implements


class Viewlet(ViewletBase):
    """Base viewlet"""
    implements(IViewlet)

    def _handle_repeated(self, item):
        raise NotImplementedError('Handle item')

    def repeated(self, item=None):
        self._handle_repeated(item)
        return self.render()
