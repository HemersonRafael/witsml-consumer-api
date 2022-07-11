# WITSML CONSUMER API

This RESTFul API consumes data from a Wellsite Information Transfer Standard Markup Language (WITSML) 
server and provides responses in format JSON. Therefore abstracting the complexity of using directly 
the WITSML.

Supported WITSML Data version: 1.4.1.1

Supported WITSML data objects based on Standards maintained by [Energistics](https://www.energistics.org/witsml-data-standards/):

- Log
- Well
- Wellbore

Supported WMLS_GetCap Function

Purpose: Returns the capServer object that describes the capabilities of the server for one Data Schema
Version.

Therefore it is possible to get more information about the limitations of the WITSML server.

## **Attention with Security**

Before deploying in production is necessary choice one way among many
ways to handle security, authentication and authorization.

Some possible options:

- [OAuth2](https://oauth.net/2/)
- [OAuth 1](https://oauth.net/1/)
- [OpenID Connect](https://openid.net/connect/)

[More information for WITSML Developers & Users](https://www.energistics.org/witsml-developers-users/)

## Getting started

This document includes instructions to get the project running in development.

### Running the project locally

#### Pre-requisites

- [Python >= 3.10 and < 3.11](https://www.python.org/)
- [Poetry >= 1.1.13](https://python-poetry.org/docs/)
- [GNU Make >= 4.3.0](https://www.gnu.org/software/make/)

#### Guide

1. Open your terminal realize the download and change to the directory to the project's root:

   ```bash
   git clone https://github.com/HemersonRafael/witsml-consumer-api.git
   cd witsml_consumer_api
   ```

2. Copy the sample environment variables file and edit them to your environment:

   ```bash
   cp .env.sample .env
   ```

    - **WITSML_SERVICE_URL** -> The WITSML storage URL. will try to connect.
    - **WITSML_USERNAME** -> The WITSML username used by [komle-plus](https://github.com/HemersonRafael/komle-plus).
    - **WITSML_PASSWORD** -> The WITSML password to be set on the user above.

3. Spawn a shell with the virtualenv activated:

   ```bash
   poetry shell
   ```

4. Install all packages specified:

   ```bash
   poetry install
   or
   make install
   ```

5. Run your project:

   ```bash
   poetry run uvicorn witsml_consumer_rest_api.main:app --host localhost --port 8080 --reload --log-level debug
   or
   make run
   ```

6. Documentation will be available by  accessing the API endpoint below:

   <http://localhost:8080/docs>
   or
   <http://localhost:8080/redoc>
