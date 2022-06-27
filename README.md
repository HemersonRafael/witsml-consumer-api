# WITSML CONSUMER API
This RESTFull API consumes data from a WITSML storage.

## Getting started

This document includes instructions to get the project running in development.

### Running the project locally

#### Pre-requisites:

- [Python ">=3.10,<3.11"](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server-pt)
- [Poetry](https://python-poetry.org/docs/)


#### Guide

1. Open your terminal and change directory to the project's root:
   ```bash
   cd witsml_consumer_rest_api
   ```

2. Copy the sample environment variables file and edit them to your environment:
   ```bash
   cp .env.sample .env
   ```
    * **WITSML_SERVICE_URL** -> The WITSML storage URL. will try to connect.
    * **WITSML_USERNAME** -> The WITSML username used by [komle-plus](https://github.com/HemersonRafael/komle-plus).
    * **WITSML_PASSWORD** -> The WITSML password to be set on the user above.
<br/><br/>

3. Spawn a shell with the virtualenv activated:
   ```bash
   poetry shell
   ```

4. Install all packages specified:
   ```bash
   poetry install
   ```

5. Run your project:
   ```bash
   poetry run uvicorn witsml_consumer_rest_api.main:app --host localhost --port 8080 --reload --log-level debug
   ```

6. Documentation will be available by  accessing the API endpoint below:
   ```
   http://localhost:8080/docs
   ```
