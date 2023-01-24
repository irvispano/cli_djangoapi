from django.urls import path

from convert.views import CurrencyConvertor

urlpatterns = [
    path("convert/", CurrencyConvertor.as_view(), name="convert"),
]
