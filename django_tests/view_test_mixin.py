# article for more information:
# https://ianwaldron.com/article/20/template-tests-for-django-templateview/

# noinspection PyUnresolvedReferences
class ViewTestMixin:  # pragma: no cover
    """
    For use w/o user or permissions; public pages etc.
    """

    def _check_attr(self, attr_name):
        self.assertIsNotNone(
            getattr(self, attr_name, None),
            msg=f"The required attribute '{attr_name}' has not been set causing the test to fail."
        )

    def test_uses_correct_template(self):
        # check w/o user or perms
        self._check_attr("reversed_url")
        self._check_attr("template_name")
        response = self.client.get(self.reversed_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name)

    def test_view_url(self):
        self._check_attr("static_url")
        # response checked in correct_template so no need to use client here
        self.assertEqual(self.reversed_url, self.static_url)
