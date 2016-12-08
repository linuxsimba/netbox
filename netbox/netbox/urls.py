from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from views import home, handle_500, trigger_500
from users.views import login, logout


handler500 = handle_500

schema_view = get_swagger_view(title="Netbox API")

_patterns = [

    # Default page
    url(r'^$', home, name='home'),

    # Login/logout
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    # Apps
    url(r'^circuits/', include('circuits.urls', namespace='circuits')),
    url(r'^dcim/', include('dcim.urls', namespace='dcim')),
    url(r'^ipam/', include('ipam.urls', namespace='ipam')),
    url(r'^secrets/', include('secrets.urls', namespace='secrets')),
    url(r'^tenancy/', include('tenancy.urls', namespace='tenancy')),
    url(r'^profile/', include('users.urls', namespace='users')),

    # API
    url(r'^api/circuits/', include('circuits.api.urls', namespace='circuits-api')),
    url(r'^api/dcim/', include('dcim.api.urls', namespace='dcim-api')),
    url(r'^api/ipam/', include('ipam.api.urls', namespace='ipam-api')),
    url(r'^api/secrets/', include('secrets.api.urls', namespace='secrets-api')),
    url(r'^api/tenancy/', include('tenancy.api.urls', namespace='tenancy-api')),
    url(r'^api/docs/', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Error testing
    url(r'^500/$', trigger_500),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

]

# Prepend BASE_PATH
urlpatterns = [
    url(r'^{}'.format(settings.BASE_PATH), include(_patterns))
]
