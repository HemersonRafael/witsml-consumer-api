# -*- coding: utf-8 -*-
"""Implementation of the base schema."""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator


class Base(BaseModel):
    xmlAttribs: bool = True
    OptionsIn: str = Field(
        default='',
        example='dataVersion=1.4.1.1',
        description="""
            An OptionsIn parameter provides a mechanism for a client to pass 
            configuration information to the server.
            1) dataVersion=1.4.1.1
            2) dataVersion=1.4.1.1;maxReturnNodes=1000
            3) dataVersion=1.4.1.1;requestLatestValues=100;maxReturnNodes=1000
            Don't forget to use ";" to separate the different keywords
        """,
    )
    returnElements: str = Field(
        default='all',
        description="""Is an OptionsIn Keywords that Indicates which elements and 
            attributes are requested to be returned in addition to the data 
            object selection items
        """,
    )
    uid: Optional[str] = Field(
        example='w-42', description='Universally unique identifier.'
    )
    name: Optional[str] = Field(example='A-42', description='Name.')
    dTimCreation: Optional[datetime] = Field(
        example='2022-04-22T05:47:54.284Z',
        description='Date Time Creation.',
    )
    dTimLastChange: Optional[datetime] = Field(
        example='2022-04-22T05:47:54.284Z',
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
