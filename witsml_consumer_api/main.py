# -*- coding: utf-8 -*-
"""Main."""
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from witsml_consumer_api.config import open_api_settings
from witsml_consumer_api.routers import logs, wellbores, wells

app = FastAPI(**open_api_settings)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(logs.router, tags=['logs'])
app.include_router(wells.router, tags=['wells'])
app.include_router(wellbores.router, tags=['wellbores'])


@app.get('/', tags=['active'])
async def root() -> Any:
    return {'message': 'I am active!'}
