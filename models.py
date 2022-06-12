from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel



class Person(BaseModel):
    sex: int
    age: int
    platform: str
    favor: str
    region: str
    cash: int
