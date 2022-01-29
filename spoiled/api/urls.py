from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from spoiled.api.views import SpoiledList

urlpatterns = [
    path("spoileds/", SpoiledList.as_view(), name="api_spoiled_list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)