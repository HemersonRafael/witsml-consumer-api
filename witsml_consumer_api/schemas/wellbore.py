# -*- coding: utf-8 -*-
"""Implementation of the wellbore schema."""
from datetime import datetime
from typing import Optional

from pydantic import Field, validator

from witsml_consumer_api.schemas import Base


class Wellbore(Base):
    uidWell: Optional[str] = Field(
        example='6507/7-A-42',
        description='Universally Unique well Identifier.',
    )
    nameWell: Optional[str] = Field(
        example='6507/7-A-42', description='Name Well.'
    )
    number: Optional[str] = Field(
        example='1234-0987', description='Operator borehole number.'
    )
    statusWellbore: Optional[str] = Field(
        example='active', description='POSC wellbore status.'
    )
    isActive: Optional[bool] = Field(
        example=True,
        description="""
            True (="1" or "true") indicates that the wellbore is active.
            False (="0" or "false") indicates otherwise. It is the servers
            responsibility to set this value based on its available internal
            data (e.g., what objects are changing).
        """,
    )
    purposeWellbore: Optional[str] = Field(
        example='exploration', description='POSC wellbore purpose.'
    )
    typeWellbore: Optional[str] = Field(
        example='initial', description='type of wellbore.'
    )
    shape: Optional[str] = Field(
        example='horizontal', description='POSC wellbore trajectory shape.'
    )
    dTimKickoff: Optional[datetime] = Field(
        example='2001-03-15T13:20:00.000Z',
        description='Date and time of wellbore kickoff.',
    )
    achievedTD: Optional[bool] = Field(
        example=False,
        description="""
            True ("true" of "1") indicates that the wellbore has acheieved 
            total depth. That is, drilling has completed. False 
            ("false" or "0") indicates otherwise. Not given indicates that
            it is not known whether total depth has been reached.
        """,
    )

    @validator('statusWellbore')
    def wellbore_status_match(cls, wellbore_status):
        wellbore_states = [
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
        if wellbore_status not in wellbore_states:
            raise ValueError(
                f'statusWellbore must be in {str(wellbore_states)}!'
            )

        return wellbore_status

    @validator('purposeWellbore')
    def purpose_wellbore_match(cls, purpose_wellbore):
        purposes_wellbore = [
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
        if purpose_wellbore not in purposes_wellbore:
            raise ValueError(
                f'purposeWellbore must be in {str(purposes_wellbore)}!'
            )

        return purpose_wellbore

    @validator('typeWellbore')
    def type_welbore_match(cls, type_welbore):
        types_welbore = [
            'bypass',
            'initial',
            'redrill',
            'reentry',
            'respud',
            'sidetrack',
            'unknown',
        ]
        if type_welbore not in types_welbore:
            raise ValueError(f'typeWellbore must be in {str(types_welbore)}!')

        return type_welbore

    @validator('shape')
    def shape_match(cls, shape):
        shapes = [
            'build and hold',
            'deviated',
            'double kickoff',
            'horizontal',
            'S-shaped',
            'vertical',
            'unknown',
        ]
        if shape not in shapes:
            raise ValueError(f'shape must be in {str(shapes)}!')

        return shape
