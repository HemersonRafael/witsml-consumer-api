# -*- coding: utf-8 -*-
"""Main."""
from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from witsml_consumer_api.routers import logs, wellbores, wells
description="""
This RESTFull API consumes data from a WITSML storage.

Supported WITSML Data version: 1.4.1.1

Supported WITSML data objects based on Standards maintained by [Energistics](https://www.energistics.org/witsml-data-standards/) standards:
- Well
- Wellbore
- Log
"""
app = FastAPI(
    title="WITSML CONSUMER API",
    description=description,
    version="0.1.0",
    contact={
        "name": "Hemerson Rafael",
        "email": "rafaelpontes1995@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(logs.router)
app.include_router(wells.router)
app.include_router(wellbores.router)


@app.get('/')
async def root() -> Any:
    return {'message': 'I am active!'}


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8080,
        log_level='debug',
        reload=True,
    )
