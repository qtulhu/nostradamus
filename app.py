from fastapi import FastAPI, Depends

from auth import get_current_username

from models import Person

app = FastAPI(
    title='Nostradamus',
    description='Сервис ',
    version='1.0.0',
    docs_url='/nostradamus/docs',
    openapi_url = '/nostradamus/openapi.json'
)

@app.get('/{operation_id}')
def get_data(
    operation_id: int,
    username: str = Depends(get_current_username)):
    return 0

@app.post('/nostradamus/baza')
def baza(
params: Person,
username: str = Depends(get_current_username)):

    return 0

@app.post('/nostradamus/ca')
def ca(
params: Person,
username: str = Depends(get_current_username)):

    return 0


@app.post('/nostradamus/top')
def top(
params: Person,
username: str = Depends(get_current_username)):

    return 0
