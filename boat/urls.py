from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from boat.apps import BoatConfig
from boat.views import BoatListView

app_name = BoatConfig.name

urlpatterns = [
    path('', BoatListView.as_view(), name='boat_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
