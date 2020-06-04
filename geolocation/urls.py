from django.urls import path, re_path

from .views import AgencyLocationView, SalesmanLocationHisView

app_name = 'geolocation'

urlpatterns = [
    path("", AgencyLocationView.as_view())
]
