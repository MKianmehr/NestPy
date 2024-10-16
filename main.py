from fastapi import FastAPI
from app.modules.users.user_module import UserModule


app = FastAPI()

app.include_router(UserModule.router)
