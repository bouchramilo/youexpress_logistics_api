

# fonction de test de creation d'un livreru
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
  
    
# test de endpoint de récupération un livreur
def test_read_livreur(client):
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
    livreur_id = data["id"]
    
    # Lire le livreur créé
    response = client.get(f"/livreurs/{livreur_id}")
    assert response.status_code == 200
    read_data = response.json()
    assert read_data["id"] == livreur_id


# test de endpoint de récupération des livreurs
def test_read_livreurs(client):
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
    livreur_id = data["id"]
    
    # Lire tous les livreurs
    response = client.get(f"/livreurs/")
    assert response.status_code == 200
    read_data = response.json()
    assert isinstance(read_data, list)
    assert len(read_data) >= 1