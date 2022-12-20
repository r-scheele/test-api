from functools import partial

from fastapi import FastAPI
from fastapi_opa import OPAMiddleware
import os

# import request from starlette
from starlette.requests import Request

# from pygeoapi.starlette_app import app as pygeoapi
from starlette.middleware.cors import CORSMiddleware
from fastapi_opa import OPAConfig
from fastapi_opa.auth import OIDCAuthentication
from fastapi_opa.auth import OIDCConfig

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


opa_host = "http://localhost:8181"

oidc_config = OIDCConfig(
    well_known_endpoint="http://localhost:8080/auth/realms/pygeoapi/.well-known/openid-configuration",
    app_uri="http://localhost:8000",
    client_id="pygeoapi-client",
    client_secret="81412735-95a5-4dcc-9d81-130d05e8ead5",
    get_user_info=True,
)
oidc_auth = OIDCAuthentication(oidc_config)
opa_config = OPAConfig(authentication=oidc_auth, opa_host=opa_host)


app.add_middleware(
    OPAMiddleware,
    config=opa_config,
)


@app.get("/users/{username}")
async def test1():
    return {"message": "Hello World from test1"}


@app.get("/users/{groupname}/{username}")
async def test2():
    return {"message": "Hello World from test2"}


@app.post("/users/{username}")
async def test2():
    return {"message": "Hello World from test2"}
