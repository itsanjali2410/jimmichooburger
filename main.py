from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#data: ingredients
items = {
    "bun": 10,        
    "patty": 1000.0,  
    "lettuce": 5,     
    "ketchup": 500.0, 
    "tomato": 5       
}

# Required quantities for one burger
required_quantities = {
    "bun": 1,         
    "patty": 150.0,   
    "lettuce": 1,     
    "ketchup": 20.0,  
    "tomato": 1       
}


class Ingredients(BaseModel):
    bun: int
    tomato: int
    ketchup: int
    patty: int
    lettuce: int

@app.get("/")
async def get_burgers():#maximum number of burgers that can be served
    burgers_served = min(items["bun"], items["tomato"], items["ketchup"], items["patty"], items["lettuce"])
    return {"burgers_served": burgers_served}

@app.post("/")
async def update_ingredients(ingredients: Ingredients): #ingredient quantities with the provided values
    items["bun"] = ingredients.bun
    items["tomato"] = ingredients.tomato
    items["ketchup"] = ingredients.ketchup
    items["patty"] = ingredients.patty
    items["lettuce"] = ingredients.lettuce

    #after updating items count
    burgers_served = min(items["bun"], items["tomato"], items["ketchup"], items["patty"], items["lettuce"])
    return {"burgers_served": burgers_served, "updated_ingredients": items}
