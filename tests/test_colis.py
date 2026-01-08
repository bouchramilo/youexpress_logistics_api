def test_create_colis(client):
    client_data = {
        "nom": "Benali",
        "prenom": "Omar",
        "email": "omar.benali@example.com",
        "adresse": "123 Rue de Rabat",
        "telephone": "0611223344",
        "ville": "Casablanca"
    }
    client_res = client.post("/clients/", json=client_data)
    assert client_res.status_code == 200

    client_id = client_res.json()["id"]

 
    destinataire_data = {
        "nom": "Fassi",
        "prenom": "Sara",
        "email": "sara.fassi@example.com",
        "telephone": "0655667788",
        "adresse": "45 Av Mohammed V"
    }
    dest_res = client.post("/destinataires/", json=destinataire_data)
    assert dest_res.status_code == 200

    destinataire_id = dest_res.json()["id"]
    colis_data = {
        "description": "Electronic Components",
        "poids": 2.5,
        "statut": "PENDING",
        "ville_destination": "Tanger",
        "client_id": client_id,         # Link to the client we just made
        "destinataire_id": destinataire_id # Link to the destinataire we just made
    }

    colis_response = client.post("/colis/", json=colis_data)

    assert colis_response.status_code == 200
    data = colis_response.json()
    
    assert data["description"] == "Electronic Components"
    assert data["client_id"] == client_id
    assert data["destinataire_id"] == destinataire_id
    assert "id" in data