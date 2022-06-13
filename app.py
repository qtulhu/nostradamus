from fastapi import FastAPI, Depends

from auth import get_current_username

from fastapi.middleware.cors import CORSMiddleware

import service
from models import *

app = FastAPI(
    title='Nostradamus',
    description='Сервис по подбору каналов рекламы',
    version='1.0.1',
    docs_url='/nostradamus/docs',
    openapi_url = '/nostradamus/openapi.json'
)

@app.get('/nostradamus/{topic}')
def test(
topic: str,
username: str = Depends(get_current_username)):
    return service.get_data_from_vk(topic)

@app.post('/nostradamus/')
def main_request(
params: MainRequest,
username: str = Depends(get_current_username)):
    print(params)
    data = service.main_service1(params)
    return data

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://10.0.36.22:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
