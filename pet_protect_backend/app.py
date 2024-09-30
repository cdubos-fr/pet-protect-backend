"""Application module."""

from fastapi import FastAPI

from pet_protect_backend.routers import graphql

app = FastAPI()

app.include_router(graphql.router, prefix='/graphql')
