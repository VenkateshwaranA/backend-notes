from fastapi import FastAPI
from routes.route import router
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # allow these origins
    allow_credentials=True,
    allow_methods=["*"],          # allow all methods (POST, GET, etc.)
    allow_headers=["*"],          # allow all headers
)
app.include_router(router)


