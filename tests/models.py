from __future__ import annotations

from typing import Dict, List

from polyfactory.factories.pydantic_factory import ModelFactory
from pydantic import BaseModel


class Individual(BaseModel):
    first_name: str
    last_name: str
    id: str
    optional: str | None
    complex: Dict[str, List[Dict[str, str]]]


class IndividualFactory(ModelFactory[Individual]):
    __model__ = Individual
