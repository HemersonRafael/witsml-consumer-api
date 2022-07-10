# -*- coding: utf-8 -*-
"""Configurations."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    WITSML_SERVICE_URL: str
    WITSML_USERNAME: str
    WITSML_PASSWORD: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')

description: str = """
This RESTFull API consumes data from a WITSML storage.

Supported WITSML Data version: 1.4.1.1

Supported WITSML data objects based on Standards maintained by [Energistics](https://www.energistics.org/witsml-data-standards/):
- Log
- Well
- Wellbore

Don't forget to set the environment variables:
* **WITSML_SERVICE_URL** -> The WITSML storage URL. will try to connect.
* **WITSML_USERNAME** -> The WITSML username used by [komle-plus](https://github.com/HemersonRafael/komle-plus).
* **WITSML_PASSWORD** -> The WITSML password to be set on the user above.

**Attention with Security**

Before deploying in production is necessary choice one way among many 
ways to handle security, authentication and authorization.

Some possible options:
- [OAuth2](https://oauth.net/2/)
- [OAuth 1](https://oauth.net/1/)
- [OpenID Connect](https://openid.net/connect/)

[More](https://github.com/HemersonRafael/witsml-consumer-api)
"""

tags_metadata: list = [
    {
        'name': 'active',
        'description': 'To check if the API is active.',
    },
    {
        'name': 'logs',
        'description': 'The log object is used to capture the curves on a well log.',
        'externalDocs': {
            'description': 'Logs external docs',
            'url': 'http://w3.energistics.org/schema/WITSML_v1.4.1.1_Data_Schema_with_Raster_v1.0/witsml_v1.4.1.1_data/doc/witsml_schema_overview.html#_log_schema',
        },
    },
    {
        'name': 'wells',
        'description': 'The well object is used to capture the general information about a well.',
        'externalDocs': {
            'description': 'Wells external docs',
            'url': 'http://w3.energistics.org/schema/WITSML_v1.4.1.1_Data_Schema_with_Raster_v1.0/witsml_v1.4.1.1_data/doc/witsml_schema_overview.html#_well_schema',
        },
    },
    {
        'name': 'wellbores',
        'description': 'The wellbore object is used to capture the general information about a wellbore.',
        'externalDocs': {
            'description': 'Wellbores external docs',
            'url': 'http://w3.energistics.org/schema/WITSML_v1.4.1.1_Data_Schema_with_Raster_v1.0/witsml_v1.4.1.1_data/doc/witsml_schema_overview.html#_wellbore_schema',
        },
    },
]

open_api_settings = {
    'title': 'WITSML CONSUMER API',
    'version': '0.1.0',
    'description': description,
    'contact': {
        'name': 'Hemerson Rafael',
        'email': 'rafaelpontes1995@gmail.com',
        'url': 'https://www.linkedin.com/in/hemerson-rafael/',
    },
    'license_info': {
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
    'openapi_tags': tags_metadata,
}
