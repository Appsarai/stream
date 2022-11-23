import os

class Config:
    API_ID = int( os.getenv("api_id","1031294") )
    API_HASH = os.getenv("api_hash","a6cb99c3647b389da9ce131bfbad60a8")
    CHANNEL = int( os.getenv("channel_files_chat_id","97608294") )
    CHANNEL_USERNAME = os.getenv("channel_username","myup1390")
    TOKEN = os.getenv("token","5372495331:AAEjQK3N1xJqTb-Tun8U6WUi2J8dCKeeDZA")
    DOMAIN  = os.getenv("domain","http://localhost")