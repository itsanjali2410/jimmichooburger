from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_update_and_get_burgers():
    initial_response = client.get("/")
    assert initial_response.status_code == 200

    #this will test the endpoint
    updated_ingredients = {
        "bun": 8,
        "tomato": 6,
        "ketchup": 100,
        "patty": 300,
        "lettuce": 4
    }
    response = client.post("/", json=updated_ingredients)
    assert response.status_code == 200

    burgers_served = min(updated_ingredients.values())
    assert response.json()["burgers_served"] == burgers_served


    final_response = client.get("/")
    assert final_response.status_code == 200
    assert final_response.json()["burgers_served"] == burgers_served
