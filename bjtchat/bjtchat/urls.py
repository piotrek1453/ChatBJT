# adresy i przekierowania

from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url='chat/')),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]
