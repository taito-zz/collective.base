from collective.base.interfaces import IViewlet
from collective.base.viewlet import Viewlet

import mock
import unittest


class ViewletTestCase(unittest.TestCase):
    """TestCase for Viewlet"""

    def test_subclass(self):
        from plone.app.layout.viewlets.common import ViewletBase as Base
        self.assertTrue(issubclass(Viewlet, Base))
        from zope.viewlet.interfaces import IViewlet as Base
        self.assertTrue(issubclass(IViewlet, Base))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        context = mock.Mock()
        instance = Viewlet(context, None, None, None)
        self.assertTrue(verifyObject(IViewlet, instance))

    def test_repeated(self):
        context = mock.Mock()
        instance = Viewlet(context, None, None, None)
        with self.assertRaises(NotImplementedError):
            instance.repeated()

        instance._handle_repeated = mock.Mock()
        instance.render = mock.Mock()
        instance.repeated()
        self.assertTrue(instance.render.called)
