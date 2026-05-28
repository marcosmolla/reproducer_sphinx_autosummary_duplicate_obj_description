"""Base module with a generic pydantic model."""

from __future__ import annotations

from abc import abstractmethod

import pydantic


class IState:
    """Marker interface for state objects."""


class IBase[TState: IState](pydantic.BaseModel):
    """A generic pydantic base using PEP 695 type parameter syntax."""

    model_config = pydantic.ConfigDict(frozen=True)

    @abstractmethod
    def create_state(self) -> TState:
        """Create a state instance."""
