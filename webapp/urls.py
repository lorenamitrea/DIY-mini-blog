from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todolist.urls')),
    path('accounts/', include(urls)),
    path('', RedirectView.as_view(url='todo/')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

