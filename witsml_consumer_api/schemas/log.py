# -*- coding: utf-8 -*-
"""Implementation of the log schema."""
from datetime import datetime
from typing import Optional

from pydantic import Field, validator

from witsml_consumer_api.schemas import Base


class Log(Base):
    uidWell: Optional[str] = Field(
        example='w-42', description='Universally Unique well Identifier.'
    )
    uidWellbore: Optional[str] = Field(
        example='w-42-1', description='Universally Unique wellbore Identifier'
    )
    nameWell: Optional[str] = Field(example='A-42', description='Name Well.')
    nameWellbore: Optional[str] = Field(
        example='A-42', description='Name Wellbore.'
    )
    dataGroup: Optional[str] = Field(
        example='A-42',
        description="""
            The name of the grouping represented by curves in this log. 
            A group represents a named combination of curves and the 
            curves in a particular log should be represented in that list.
        """,
    )
    serviceCompany: Optional[str] = Field(
        example='A-42',
        description='Name of contractor who provided the service.',
    )
    creationDate: Optional[datetime] = Field(
        example='2001-06-18T13:20:00.000Z',
        description='Date and time that the log was created.',
    )
    indexType: Optional[str] = Field(
        example='measured depth', description='Primary index type.'
    )
    objectGrowing: Optional[bool] = Field(
        example=True, description='The growing state of the object.'
    )
    startIndex: Optional[float] = Field(
        example=499,
        description="""
            When the log header defines the direction as "Increasing", the 
            startIndex is the starting (minimum) index value at which the 
            first non-null data point is located. When the log header 
            defines the direction as "Decreasing", the startIndex is the 
            starting (maximum) index value at which the first non-null 
            data point is located. Either a quantity index set 
            (start and end) or a date time index set must be given. If 
            both sets are given then "indexType" and "indexCurve" must 
            represent an elapsed time from "startDateTimeIndex".
        """,
    )
    endIndex: Optional[float] = Field(
        example=509.01,
        description="""
            When the log header defines the direction as "Increasing", 
            the endIndex is the ending (maximum) index value at which the last 
            non-null data point is located. When the log header defines the 
            direction as Decreasing, the endIndex is the ending (minimum) index value 
            at which the last non-null data point is located. This is an API 
            "structural-range" query parameter for growing objects.
        """,
    )
    startDateTimeIndex: Optional[datetime] = Field(
        example='2001-07-15T15:30:00.000Z',
        description="""
            When the log header defines the direction as "Increasing", the startIndex
            is the starting (minimum) index value at which the first non-null
            data point is located. When the log header defines the direction as 
            "Decreasing", the startIndex is the starting (maximum) index value at 
            which the first non-null data point is located. Either a quantity index
            set (start and end) or a date time index set must be given. If both sets
            are given then "indexType" and "indexCurve" must represent an elapsed 
            time from "startDateTimeIndex".
        """,
    )
    endDateTimeIndex: Optional[datetime] = Field(
        example='2001-07-15T16:30:00.000Z',
        description="""
            When the log header defines the direction as "Increasing", the
            endIndex is the ending (maximum) index value at which the last
            non-null data point is located. When the log header defines the
            direction as Decreasing, the endIndex is the ending (minimum) 
            index value at which the last non-null data pointis located.
        """,
    )
    direction: Optional[str] = Field(
        example='increasing',
        description='The sort order of the data row index values in the XML instance.',
    )
    indexCurve: Optional[str] = Field(
        example='Mdepth', description='The mnemonic of the index curve.'
    )

    @validator('indexType')
    def index_type_match(cls, index_type):
        index_types = [
            'date time',
            'elapsed time',
            'length',
            'measured depth',
            'vertical depth',
            'other',
            'unknown',
        ]
        if index_type not in index_types:
            raise ValueError(f'indexType must be in {str(index_types)}!')

        return index_type

    @validator('direction')
    def direction_match(cls, direction):
        directions = ['decreasing', 'increasing', 'unknown']
        if direction not in directions:
            raise ValueError(f'direction must be in {str(directions)}!')

        return direction
