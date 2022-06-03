from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-original/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('login.urls')),
    path('about/', include('about.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "coderblog.views.page_not_found_view"
handler401 = "coderblog.views.page_unauthorized"
handler400 = "coderblog.views.page_bad_request"
handler403 = "coderblog.views.page_forbidden"
handler500 = "coderblog.views.internal_server_error"
