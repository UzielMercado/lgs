from django.contrib import admin
from django.urls import path
from core import views as core_views
from hero import views as hero_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name="home"),
    path('productos/', core_views.productos, name="productos"),
    path('cartas/', core_views.cartas, name="cartas"),
    path('figuras/', hero_views.figuras, name="figuras")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
