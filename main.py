from typing import Optional
from fastapi import FastAPI
from RPA.Excel.Files import Files
from RPA.Tables import Tables

myapp = FastAPI()

@myapp.get("/")
def tr():
    return {
        "data" : {
            "name" : "Raj",
            "Age" : "24" ,
            "Location" : "BLR"
        }
    }

@myapp.get("/{id}/project")
def project(id :bool):
    return {"project":f"Fast API learn : {id}"}

@myapp.post("/ch")
def get_project(limit :int = 15, size :int = 15, l : Optional[str] = None):
    if limit == size:
        return {"data":f"size of {size} with limit {limit} matches with lopt= {l} "}
    else:
        return { "data": f"size of {size} doesn't match limit {limit} with lopt= {l}"}