from typing import (
    List,
    Optional,
)

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session
#
import tables

from models import DataBaseModel
from database import get_session


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_data(self):
        operations = (self.session.query(tables.Clients).filter(tables.Clients.purchase_count == '48').all())
          # .filter(tables.Operation.user_id == user_id)
        # data = DataBaseModel(operations)
        print(operations[0]._asdict())
        return operations



# SELECT

# def percent_age():
#     pass
#
#
# def percent_sex():
#     pass
#
#
# def avg_bill():
#     pass
