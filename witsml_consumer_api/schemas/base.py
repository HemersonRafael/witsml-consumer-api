# -*- coding: utf-8 -*-
"""Implementation of the base schema."""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator


class Base(BaseModel):
    xmlAttribs: bool = True
    OptionsIn: str = ''
    returnElements: str = Field(
        default='requested', description='Return Elements'
    )
    uid: Optional[str] = Field(
        exempla='w-42', description='Universally unique identifier.'
    )
    name: Optional[str] = Field(exempla='A-42', description='Name.')
    dTimCreation: Optional[datetime] = Field(
        exempla='2022-04-22T05:47:54.284Z',
        description='Date Time Creation.',
    )
    dTimLastChange: Optional[datetime] = Field(
        exempla='2022-04-22T05:47:54.284Z',
        description='Date Time Last Change.',
    )

    @validator('returnElements')
    def return_elements_match(cls, option):
        options = [
            'all',
            'id-only',
            'header-only',
            'data-only',
            'station-location-only',
            'latest-change-only',
            'requested',
        ]
        if option not in options:
            raise ValueError(f'returnElements must be in {str(options)}!')

        return option
