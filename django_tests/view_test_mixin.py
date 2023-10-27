# article for more information:
# https://ianwaldron.com/article/20/template-tests-for-django-templateview/

# noinspection PyUnresolvedReferences, PyPep8Naming
class ViewTestMixin:  # pragma: no cover
    """
    For use w/o user or permissions; public pages etc.
    """

    @classmethod
    def setUpTestData(cls):
        cls.template_name = None
        cls.reversed_url = None
        cls.static_url = None

    def test_uses_correct_template(self):
        # check w/o user or perms
        self.assertIsNotNone(getattr(self, "template_name", None))
        self.assertIsNotNone(getattr(self, "reversed_url", None))
        response = self.client.get(self.reversed_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name)

    def test_view_url(self):
        # response checked in correct_template so no need to use client here
        self.assertIsNotNone(getattr(self, "static_url", None))
        self.assertEqual(self.reversed_url, self.static_url)
