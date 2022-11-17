from dotenv import load_dotenv
from pydantic import BaseSettings
import os
load_dotenv()


class Settings(BaseSettings):
    HOST: str = os.getenv('HOST') 
    SECRET_KEY: str = os.getenv('SECRET_KEY') 
    ALGORITHM: str = os.getenv('ALGORITHM')  
    ACCESS_TOKEN_EXPIRE_MINUTES: str = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES') 
    PORT: str = os.getenv('PORT')  
    URI: str = os.getenv('URI')  
    SLACK_ERRORS: str = os.getenv('SLACK_ERRORS') 

