from typing import Optional

from pydantic import Field, validator

from witsml_consumer_rest_api.schemas import Base


class Log(Base):
    uidWell: Optional[str] = Field(exemplo='w-42', description='Uid Well.')
    uidWellbore: Optional[str] = Field(
        exemplo='w-42-1', description='Uid Wellbore.'
    )
    nameWell: Optional[str] = Field(exemplo='A-42', description='Name Well.')
    nameWellbore: Optional[str] = Field(
        exemplo='A-42', description='Name Wellbore.'
    )
    dataGroup: Optional[str] = Field(
        exemplo='A-42',
        description='The name of the grouping represented by curves in this log. A group represents a named combination of curves and the curves in a particular log should be represented in that list.',
    )
    serviceCompany: Optional[str] = Field(
        exemplo='A-42',
        description='Name of contractor who provided the service.',
    )
    creationDate: Optional[str] = Field(
        exemplo='2001-06-18T13:20:00.000Z',
        description='Date and time that the log was created.',
    )
    indexType: Optional[str] = Field(
        exemplo='measured depth', description='Primary index type.'
    )
    startIndex: Optional[float] = Field(
        exemplo=499,
        description='When the log header defines the direction as "Increasing", the startIndex is the starting (minimum) index value at which the first non-null\
                  data point is located. When the log header defines the direction as "Decreasing", the startIndex is the starting (maximum) index value at which the first\
                  non-null data point is located. Either a quantity index set (start and end) or a date time index set must be given. If both sets are given then "indexType" and\
                  "indexCurve" must represent an elapsed time from "startDateTimeIndex".',
    )
    endIndex: Optional[float] = Field(
        exemplo=509.01,
        description='When the log header defines the direction as "Increasing", the endIndex is the ending (maximum) index value at which the last non-null data\
                  point is located. When the log header defines the direction as Decreasing, the endIndex is the ending (minimum) index value at which the last non-null data point\
                  is located. This is an API "structural-range" query parameter for growing objects.',
    )
    startDateTimeIndex: Optional[str] = Field(
        exemplo='2001-07-15T15:30:00.000Z',
        description='When the log header defines the direction as "Increasing", the startIndex is the starting (minimum) index value at which the first non-null\
                  data point is located. When the log header defines the direction as "Decreasing", the startIndex is the starting (maximum) index value at which the first\
                  non-null data point is located. Either a quantity index set (start and end) or a date time index set must be given. If both sets are given then "indexType" and\
                  "indexCurve" must represent an elapsed time from "startDateTimeIndex". ',
    )
    endDateTimeIndex: Optional[str] = Field(
        exemplo='2001-07-15T16:30:00.000Z',
        description='When the log header defines the direction as "Increasing", the endIndex is the ending (maximum) index value at which the last non-null data\
                  point is located. When the log header defines the direction as Decreasing, the endIndex is the ending (minimum) index value at which the last non-null data point\
                  is located.',
    )
    direction: Optional[str] = Field(
        exemplo='increasing',
        description='The sort order of the data row index values in the XML instance.',
    )
    indexCurve: Optional[str] = Field(
        exemplo='Mdepth', description='The mnemonic of the index curve.'
    )
    logData: Optional[dict]

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
        if not index_type in index_types:
            raise ValueError(f'indexType must be in {str(index_types)}!')

        return index_type

    @validator('direction')
    def direction_match(cls, direction):
        directions = ['decreasing', 'increasing', 'unknown']
        if not direction in directions:
            raise ValueError(f'direction must be in {str(directions)}!')

        return direction
