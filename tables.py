from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
    VARCHAR,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Clients(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    client_id = Column(VARCHAR)
    gender = Column(VARCHAR)
    birth_date = Column(VARCHAR)
    create_date = Column(VARCHAR)
    nonresident_flag = Column(VARCHAR)
    businessman_flag = Column(VARCHAR)
    city = Column(VARCHAR)
    term = Column(VARCHAR)
    contract_sum = Column(VARCHAR)
    product_category_name = Column(VARCHAR)
    card_type_name = Column(VARCHAR)
    start_date = Column(VARCHAR)
    fact_close_date = Column(VARCHAR)
    purchase_sum = Column(VARCHAR)
    purchase_count = Column(Integer)
    current_balance_avg_sum = Column(VARCHAR)
    current_balance_sum = Column(VARCHAR)
    current_debit_turn_sum = Column(VARCHAR)
    current_credit_turn_sum = Column(VARCHAR)
    card_type = Column(VARCHAR)
    interests = Column(VARCHAR)
