# -*- coding: utf-8 -*-
"""Implementation of the well schema."""
from datetime import datetime
from typing import Optional

from pydantic import Field, validator

from witsml_consumer_api.schemas import Base


class Well(Base):
    field: Optional[str] = Field(
        example='6507/7-A-42',
        description='Name of the field in which the well is located.',
    )
    country: Optional[str] = Field(
        example='Big Field',
        description='Country in which well is located.',
    )
    state: Optional[str] = Field(
        example='TX',
        description='State or province in which well is located.',
    )
    county: Optional[str] = Field(
        example='Montgomery',
        description='County in which the well is located.',
    )
    region: Optional[str] = Field(
        example='Region Name', description='Geo-political region.'
    )
    district: Optional[str] = Field(
        example='District Name', description='Geo-political district name.'
    )
    block: Optional[str] = Field(
        example='Block Name',
        description='Block name in which well is located.',
    )
    operator: Optional[str] = Field(
        example='Operating Company', description='Operator company name.'
    )
    operatorDiv: Optional[str] = Field(
        example='Division Name',
        description='Division of operator company.',
    )
    numAPI: Optional[str] = Field(
        example='123-543-987AZ',
        description='American Petroleum Institute well number.',
    )
    statusWell: Optional[str] = Field(
        example='drilling', description='POSC Well status.'
    )
    purposeWell: Optional[str] = Field(
        example='exploration', description='POSC Well purpose.'
    )
    dTimSpud: Optional[datetime] = Field(
        example='2001-05-31T08:15:00.000Z',
        description='Date and time at which well was spudded.',
    )
    dTimPa: Optional[datetime] = Field(
        example='2001-07-15T15:30:00.000Z',
        description='Date and time at which well was plugged and abandoned.',
    )

    @validator('statusWell')
    def well_status_match(cls, well_status):
        well_states = [
            'abandoned',
            'active',
            'active -- injecting',
            'active -- producing',
            'completed',
            'drilling',
            'partially plugged',
            'permitted',
            'plugged and abandoned',
            'proposed',
            'sold',
            'suspended',
            'temporarily abandoned',
            'testing',
            'tight',
            'working over',
            'unknown',
        ]
        if well_status not in well_states:
            raise ValueError(f'statusWell must be in {str(well_states)}!')

        return well_status

    @validator('purposeWell')
    def purpose_well_match(cls, purpose_well):
        purposes_well = [
            'appraisal',
            'appraisal -- confirmation appraisal',
            'appraisal -- exploratory appraisal',
            'exploration',
            'exploration -- deeper-pool wildcat',
            'exploration -- new-field wildcat',
            'exploration -- new-pool wildcat',
            'exploration -- outpost wildcat',
            'exploration -- shallower-pool wildcat',
            'development',
            'development -- infill development',
            'development -- injector',
            'development -- producer',
            'fluid storage',
            'fluid storage -- gas storage',
            'general srvc',
            'general srvc -- borehole re-acquisition',
            'general srvc -- observation',
            'general srvc -- relief',
            'general srvc -- research',
            'general srvc -- research -- drill test',
            'general srvc -- research -- strat test',
            'general srvc -- waste disposal',
            'mineral',
            'unknown',
        ]
        if purpose_well not in purposes_well:
            raise ValueError(f'purposeWell must be in {str(purposes_well)}!')

        return purpose_well
