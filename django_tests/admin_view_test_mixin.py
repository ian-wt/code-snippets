# article for more information:
# https://ianwaldron.com/article/22/template-tests-for-django-templateview-requiring-staff-permissions/

# noinspection PyUnresolvedReferences
class AdminViewTestMixin:  # pragma: no cover

    def _check_attr(self, attr_name):
        self.assertIsNotNone(
            getattr(self, attr_name, None),
            msg=f"The required attribute '{attr_name}' has not been set causing the test to fail."
        )

    def test_staff_only(self):
        # -- with reversed url --
        self._check_attr("perms")
        self._check_attr("reversed_url")
        self._check_attr("standard_user")
        self._check_attr("staff_user")

        # test 403 for non-staff, but has perms
        self.standard_user.user_permissions.add(*self.perms)
        self.client.force_login(self.standard_user)
        response = self.client.get(self.reversed_url)
        self.assertEqual(response.status_code, 403)

        if self.perms:
            # test 403 for is-staff, but no perms
            # only works if one or more permissions is present
            self.client.force_login(self.staff_user)
            response = self.client.get(self.reversed_url)
            self.assertEqual(response.status_code, 403)

        # test 200 for is-staff and has perms

        # add each permission one at a time so that we know a good status code isn't granted for anything
        #   less than full permission

        # since has_perms uses strings and not the actual permission objects, we need to convert the permissions to
        #   a list of strings for the test
        perm_strings = [f"{p.content_type.app_label}.{p.codename}" for p in self.perms]
        for perm in self.perms:
            self.staff_user.user_permissions.add(perm)
            self.client.force_login(self.staff_user)
            response = self.client.get(self.reversed_url)
            if self.staff_user.has_perms(perm_strings):
                # all perms have been added to the user so this should be the last item and the status code
                #   should be 200
                self.assertEqual(response.status_code, 200)
            else:
                # we're at some stage user perms < total perms
                # we should get permission denied 403
                self.assertEqual(response.status_code, 403)

    def test_view_url(self):
        # we already know we have a good status code with the reversed url if test_staff_only hasn't already failed
        # so, just test the reversed url against the static url to ensure the reversed url exists where we think it
        #   should
        self._check_attr("reversed_url")
        self._check_attr("static_url")
        self.assertEqual(self.reversed_url, self.static_url)

    def test_uses_correct_template(self):
        self._check_attr("perms")
        self._check_attr("staff_user")
        self._check_attr("reversed_url")
        self._check_attr("template_name")
        self.staff_user.user_permissions.add(*self.perms)
        self.client.force_login(self.staff_user)
        response = self.client.get(self.reversed_url)
        self.assertEqual(response.status_code, 200)  # this has already been tested above
        self.assertTemplateUsed(response, self.template_name)
