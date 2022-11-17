from pydantic import BaseSettings

class Message(BaseSettings):
    msg_error_add:str= "the item hasn't been saved"
    msg_error_update:str = ''
    msg_error_delete:str = "the article wasn't deleted"
    msg_delete:str = 'the article has been deleted'
    msg_add:str = 'item was been saved'
    msg_get:str = 'Data sent'
    msg_error_dafault:str = 'An error has occurred,send email israeldillanes2@gmail.com'
    msg_update:str = "the article has been modified"
    msg_idInvalid:str = 'The Id is invalid'
    