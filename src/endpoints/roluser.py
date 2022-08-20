from fastapi import APIRouter
from fastapi import Query
from fastapi import FastAPI, Response, status,HTTPException
from src.models.roluser import RolUserModel
from typing import Optional
import requests
import json


import logging

logger = logging.getLogger(__name__)  # the __name__ resolve to "uicheckapp.services"
                                      # This will load the uicheckapp logger


#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/roluser",
    tags=["roluser"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    url = 'https://6300e253e71700618a30685c.mockapi.io/roleUsers/roleUsers'
    response = requests.get(url, {}, timeout=5)
    logger.info("Hola Rol usuarios")
    return {"encryptedToken": response.json() }

@router.get("/{encryptedToken}")
async def read_user(encryptedToken: str):
    url = 'https://6300e253e71700618a30685c.mockapi.io/roleUsers/roleUsers'+encryptedToken
    response = requests.get(url, {}, timeout=5)
    if(response.status_code==  500):
     raise HTTPException(status_code=204, detail="Item not found")
    jsonresponse = json.loads(response.text)
    return jsonresponse


@router.post("/add")
async def add_user(rol: RolUserModel):
    url = 'https://62fd8a326e617f88deab3075.mockapi.io/infoUsers/infoUsers/'
    params = {'RolUserModel':rol}
    response = requests.post(url, params = params, timeout=5)
    jsonresponse = json.loads(response.text)
    return jsonresponse


@router.put("/update/{idUsuario}")
async def read_user(rol: RolUserModel,encryptedToken: str):
    url = 'https://62fd8a326e617f88deab3075.mockapi.io/infoUsers/infoUsers/'+encryptedToken
    data=json.loads(rol.json())
    response = requests.put(url, data = data, timeout=5)
    if(response.status_code==  404):
     raise HTTPException(status_code=204, detail="Item not found")
    jsonresponse = json.loads(response.text)
    return jsonresponse


@router.delete("/delete/{encryptedToken}")
async def read_user(encryptedToken: str):
    url = 'https://62fd8a326e617f88deab3075.mockapi.io/infoUsers/infoUsers/'+encryptedToken
    response = requests.delete(url)
    if(response.status_code==  404):
     raise HTTPException(status_code=204, detail="Item not found")
    jsonresponse = json.loads(response.text)
    return jsonresponse