from ast import pattern
from typing import Optional

from pydantic import Field, validator

from witsml_consumer_rest_api.schemas import Base


class Well(Base):
    field: Optional[str] = Field(
        exemplo='6507/7-A-42',
        description='Name of the field in which the well is located.',
    )
    country: Optional[str] = Field(
        exemplo='Big Field', description='Country in which well is located.'
    )
    state: Optional[str] = Field(
        exemplo='TX', description='State or province in which well is located.'
    )
    county: Optional[str] = Field(
        exemplo='Montgomery',
        description='County in which the well is located.',
    )
    region: Optional[str] = Field(
        exemplo='Region Name', description='Geo-political region'
    )
    district: Optional[str] = Field(
        exemplo='District Name', description='Geo-political district name.'
    )
    block: Optional[str] = Field(
        exemplo='Block Name',
        description='Block name in which well is located.',
    )
    operator: Optional[str] = Field(
        exemplo='Operating Company', description='Operator company name.'
    )
    operatorDiv: Optional[str] = Field(
        exemplo='Division Name', description='Division of operator company.'
    )
    numAPI: Optional[str] = Field(
        exemplo='123-543-987AZ',
        description='American Petroleum Institute well number.',
    )
    statusWell: Optional[str] = Field(
        exemplo='drilling', description='POSC Well status.'
    )
    purposeWell: Optional[str] = Field(
        exemplo='exploration', description='POSC Well purpose.'
    )
    dTimSpud: Optional[str] = Field(
        exemplo='2001-05-31T08:15:00.000Z',
        description='Date and time at which well was spudded.',
    )
    dTimPa: Optional[str] = Field(
        exemplo='2001-07-15T15:30:00.000Z',
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
        if not well_status in well_states:
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
        if not purpose_well in purposes_well:
            raise ValueError(f'purposeWell must be in {str(purposes_well)}!')

        return purpose_well
