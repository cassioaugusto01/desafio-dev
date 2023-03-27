from pydantic import BaseModel

class TransactionBase(BaseModel):
    transaction_type: int
    date: str
    amount: float
    cpf: str
    card: str
    time: str
    owner: str
    name: str

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    store_id: int

    class Config:
        orm_mode = True
