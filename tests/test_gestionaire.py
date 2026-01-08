def test_create_gestionaire(client):
    # 1. Prepare the data
    gestionaire_data = {
        "nom": "Super Admin",
        "email": "admin@youexpress.com",
        "mot_de_passe": "secret123"
    }

    response = client.post("/gestionaires/", json=gestionaire_data)

    assert response.status_code == 201


    data = response.json()
    assert data["nom"] == "Super Admin"
    assert data["email"] == "admin@youexpress.com"
    assert "id" in data
    

    assert "mot_de_passe" not in data