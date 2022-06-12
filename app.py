from fastapi import FastAPI, Depends

from auth import get_current_username

from service import OperationsService
from models import Person

app = FastAPI(
    title='Nostradamus',
    description='Сервис по подбору каналов рекламы',
    version='1.0.1',
    docs_url='/nostradamus/docs',
    openapi_url = '/nostradamus/openapi.json'
)

@app.get('/nostradamus/baza')
def test(
username: str = Depends(get_current_username),
operations_service: OperationsService = Depends()):
    return operations_service.get_data()

@app.post('/nostradamus/baza')
def baza(
params: Person,
username: str = Depends(get_current_username),
operations_service: OperationsService = Depends()):
    return 0

@app.post('/nostradamus/ca')
def ca(
params: Person,
username: str = Depends(get_current_username),
 operations_service: OperationsService = Depends()):
    return 0


@app.post('/nostradamus/top')
def top(
params: Person,
username: str = Depends(get_current_username)):
    return 0
