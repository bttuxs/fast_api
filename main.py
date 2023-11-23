from fastapi import FastAPI
from routes import public
app = FastAPI()


app.include_router(public.router)
