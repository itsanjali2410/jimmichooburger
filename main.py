from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-app data: ingredients
items = {
    "bun": 10,        # 10 buns
    "patty": 1000.0,  # 1kg of patties
    "lettuce": 5,     # 5 leaves
    "ketchup": 500.0, # 500g of ketchup
    "tomato": 5       # 5 slices
}

# Required quantities for one burger
required_quantities = {
    "bun": 1,         # 1 bun per burger
    "patty": 150.0,   # 150g of patty per burger
    "lettuce": 1,     # 1 leaf of lettuce
    "ketchup": 20.0,  # 20g of ketchup per burger
    "tomato": 1       # 1 slice of tomato
}


class Ingredients(BaseModel):
    bun: int
    tomato: int
    ketchup: int
    patty: int
    lettuce: int

@app.get("/")
async def get_burgers():
    # Calculate the maximum number of burgers that can be served
    burgers_served = min(items["bun"], items["tomato"], items["ketchup"], items["patty"], items["lettuce"])
    return {"burgers_served": burgers_served}

@app.post("/")
async def update_ingredients(ingredients: Ingredients):
    #ingredient quantities with the provided values
    items["bun"] = ingredients.bun
    items["tomato"] = ingredients.tomato
    items["ketchup"] = ingredients.ketchup
    items["patty"] = ingredients.patty
    items["lettuce"] = ingredients.lettuce

    #after updating items count
    burgers_served = min(items["bun"], items["tomato"], items["ketchup"], items["patty"], items["lettuce"])
    return {"burgers_served": burgers_served, "updated_ingredients": items}
