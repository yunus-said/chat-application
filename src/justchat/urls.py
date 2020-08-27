from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from .view import ContactDetails
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(
        regex=r'^contacts/(?P<id>[^/]+)$',
        view=ContactDetails.as_view(),
        name='user_detail'
    ),
    path('api-auth/', include('rest_framework.urls')),
    path('chat/', include('chat.api.urls', namespace='chat')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
