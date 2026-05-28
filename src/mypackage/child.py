"""Child module with a concrete implementation that parametrizes the generic."""

from __future__ import annotations

from mypackage.base import IBase, IState


class ConcreteState(IState):
    """A concrete state implementation."""


class Child(IBase[ConcreteState]):
    """Concrete implementation that parametrizes the generic."""

    def create_state(self) -> ConcreteState:
        """Create a concrete state."""
        return ConcreteState()
