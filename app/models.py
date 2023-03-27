from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String(14), index=True)
    name = Column(String(19), index=True)
    transactions = relationship("Transaction", back_populates="store")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    transaction_type = Column(Integer)
    date = Column(String(8))
    amount = Column(Float)
    cpf = Column(String(11))
    card = Column(String(12))
    time = Column(String(6))
    store_id = Column(Integer, ForeignKey("stores.id"))

    store = relationship("Store", back_populates="transactions")
