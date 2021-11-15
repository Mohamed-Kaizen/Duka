"""Collection of pydantic model."""
from typing import Dict, Optional

from pydantic import BaseModel, Field


class SessionVariables(BaseModel):
    """Schema for session variables data."""

    x_hasura_role: str = Field(None, alias="x-hasura-role")


class HasuraAction(BaseModel):
    """Schema for hasura action data."""

    name: str


class HasuraData(BaseModel):
    """Schema for hasura data data."""

    session_variables: SessionVariables

    action: HasuraAction


class HasuraEventDate(BaseModel):
    """Schema for hasura event data."""

    old: Optional[Dict]

    new: Dict


class HasuraEvent(BaseModel):
    """Schema for hasura event data."""

    session_variables: SessionVariables

    data: HasuraEventDate


class HasuraEventTrigger(BaseModel):
    """Schema for hasura trigger event data."""

    event: HasuraEvent


class PythonGraphqlClientResponse(BaseModel):
    """Schema for python graphql client response."""

    data: Optional[dict]

    error: Optional[dict]
