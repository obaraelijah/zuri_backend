from django.urls import path

from .views import RetrieveApi

urlpatterns = [
    path("", RetrieveApi.as_view(), name="api-endpoint")
]
