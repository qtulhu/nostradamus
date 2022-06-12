from pydantic import BaseSettings
from typing import Optional

import os
import json
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    server_host: str = os.getenv('server_host')
    server_port: int = os.getenv('server_port')

    database_url: str = os.getenv('database_url')

    api_username = os.getenv('api_username')
    api_password = os.getenv('api_password')

settings = Settings()
