from typing import Optional

from pydantic import BaseModel, Field, root_validator, validator


class Base(BaseModel):
    returnElements: str = Field(
        default='requested', description='Return Elements'
    )
    uid: Optional[str] = Field(exemplo='w-42', description='uid')
    name: Optional[str] = Field(exemplo='A-42', description='name')

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
