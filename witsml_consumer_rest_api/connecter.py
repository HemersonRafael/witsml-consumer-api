from komle.soap_client import StoreClient

from witsml_consumer_rest_api.config import settings

store_client = StoreClient(
    service_url=settings.WITSML_SERVICE_URL,
    username=settings.WITSML_USERNAME,
    password=settings.WITSML_PASSWORD,
)
