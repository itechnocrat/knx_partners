from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prob.urls'))
]

# urlpatterns += ['', ]

# urlpatterns += [
#     path('prob/', include('prob.urls')),
# ]

urlpatterns += [
    path('', RedirectView.as_view(url='', permanent=True)),
]


# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
