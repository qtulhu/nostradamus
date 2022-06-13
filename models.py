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

class AgeRange(BaseModel):
    ageBegin: int
    ageEnd: int

class MoneyRange(BaseModel):
    moneyBegin: int
    moneyEnd: int

class MainRequest(BaseModel):
    sex: list
    age: list
    cash: list
    interest: list


class DataBaseModel(BaseModel):
    id: int
    client_id: str
    gender: str
    birth_date: str
    create_date: str
    nonresident_flag: str
    businessman_flag: str
    city: str
    term: str
    contract_sum: str
    product_category_name: str
    card_type_name: str
    start_date: str
    fact_close_date: str
    purchase_sum: str
    purchase_count: str
    current_balance_avg_sum: str
    current_balance_sum: str
    current_debit_turn_sum: str
    current_credit_turn_sum: str
    card_type: str
    interests: str
