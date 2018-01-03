from __future__ import unicode_literals

from django.conf import settings
from django.urls import reverse_lazy
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from users.views import UserViewSet
from devices.views import DeviceViewSet
from registrationkeys.views import RegistrationKeyViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'devices', DeviceViewSet, base_name='device')
router.register(r'registration-keys', RegistrationKeyViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^django-rq/', include('django_rq.urls')),
    url(r'^api/v1/', include('authentication.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='My API service')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    url(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
