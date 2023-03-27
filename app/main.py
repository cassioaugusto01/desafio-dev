from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from . import crud, models, schemas, parsers, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/upload/")
async def upload_cnab(file: UploadFile = File(...), db: Session = Depends(database.get_db)):
    file_content = await file.read()
    transactions = parsers.parse_cnab(file_content.decode("utf-8"))

    for transaction in transactions:
        crud.create_transaction(db, schemas.TransactionCreate(**transaction))

    return {"message": "Arquivo CNAB processado com sucesso"}