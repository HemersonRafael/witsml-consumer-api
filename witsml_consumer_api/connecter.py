# -*- coding: utf-8 -*-
"""Create storage client WITSML."""

from komle.soap_client import StoreClient

from witsml_consumer_api.config import settings

storage_client = StoreClient(
    service_url=settings.WITSML_SERVICE_URL,
    username=settings.WITSML_USERNAME,
    password=settings.WITSML_PASSWORD,
)
