def test_create_livreur(client):
    zone_data = {"nom": "Zone Sud", "ville": "Casablanca", "code_postal": "12345"}
    zone_response = client.post("/zones", json=zone_data)
    assert zone_response.status_code == 201
    zone_name = zone_response.json()["nom"]
    
    livreur_data = {
        "nom": "Sanae",
        "prenom": "Test",
        "telephone": "0600000001",
        "vehicule": "CAR",
        "zone": zone_name
    }
    
    response = client.post("/livreurs/", json=livreur_data)
    assert response.status_code == 201
    data = response.json()
    assert data["nom"] == "Sanae"
  
    
    
