from gestão.settings.base import MEDIA_ROOT
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import home_page,my_logout

urlpatterns = [
    path('', home_page, name='home'),
    path('logout', my_logout, name='my_logout' ),
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
