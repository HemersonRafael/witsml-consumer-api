# -*- coding: utf-8 -*-
"""Main."""
from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from witsml_consumer_api.routers import logs, wellbores, wells

app = FastAPI()


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
