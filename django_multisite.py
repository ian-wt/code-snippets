# article for more information:
# https://ianwaldron.com/article/37/how-to-handle-multiple-domains-in-django-with-the-sites-framework/

from django.contrib.sites.models import Site


class MultiSiteMiddleware:
    """
    Route to the appropriate root URL conf based on current host.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # this section if not using Site
        # domain = request.get_host().split(':')[0]
        # if domain.endswith('admin.example.com'):
        #     request.urlconf = 'admin.urls'
        # elif domain.endswith('app.example.com'):
        #     request.urlconf = 'app.urls'
        # elif domain.endswith('example.com'):
        #     request.urlconf = 'public.urls'

        # Note! get_current() hits the db with every request
        # Django only caches the Site object for the given request
        # possible point of optimization if requests are slow: store the
        #   Site object in sessions and only requery if get_host() has
        #   a different domain than the current Site (or upon expiration)
        domain = Site.objects.get_current(request).domain

        if domain == 'admin.example.com':
            request.urlconf = 'admin.urls'
        elif domain == 'app.example.com':
            request.urlconf = 'app.urls'
        elif domain == 'example.com':
            request.urlconf = 'public.urls'

        return self.get_response(request)