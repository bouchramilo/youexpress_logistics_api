def test_create_historiques(client):
    # Créer une zone d'abord
    zone_data = {"nom": "Zone Nord", "ville": "Rabat", "code_postal": "10000"}
    zone_response = client.post("/zones", json=zone_data)
    assert zone_response.status_code == 201
    zone_name = zone_response.json()["nom"]

    # Créer un livreur
    livreur_data = {
        "nom": "Ahmed",
        "prenom": "Test",
        "telephone": "0612345678",
        "vehicule": "MOTO",
        "zone": zone_name
    }
    livreur_response = client.post("/livreurs/", json=livreur_data)
    assert livreur_response.status_code == 201
    livreur_id = livreur_response.json()["id"]

    # Créer un client
    client_data = {
        "nom": "Client",
        "prenom": "Test",
        "email": "client.test@example.com",
        "adresse": "123 Rue Test",
        "telephone": "0687654321",
        "ville": "Rabat"
    }
    client_response = client.post("/clients/", json=client_data)
    assert client_response.status_code == 200
    client_id = client_response.json()["id"]

    # Créer un destinataire
    destinataire_data = {
        "nom": "Destinataire",
        "prenom": "Test",
        "email": "dest.test@example.com",
        "telephone": "0687654321",
        "adresse": "456 Rue Destinataire"
    }
    destinataire_response = client.post("/destinataires/", json=destinataire_data)
    assert destinataire_response.status_code == 200
    destinataire_id = destinataire_response.json()["id"]

    # Créer un colis
    colis_data = {
        "description": "Test Colis",
        "poids": 2.5,
        "statut": "CRÉE",
        "ville_destination": "Rabat",
        "client_id": client_id,
        "destinataire_id": destinataire_id
    }
    colis_response = client.post("/colis/", json=colis_data)
    assert colis_response.status_code == 200
    colis_id = colis_response.json()["id"]

    # Créer un historique
    historique_data = {
        "nouveau_statut": "EN_STOCK",
        "livreur_id": livreur_id
    }
    response = client.post(f"/colis/{colis_id}/historiques", json=historique_data)
    assert response.status_code == 201
    data = response.json()
    # Vérifier que l'ancien_statut est "CREE" (le dernier nouveau_statut du colis)
    assert data["ancien_statut"] == "CREE"
    assert data["nouveau_statut"] == "EN_STOCK"
    assert data["colis_id"] == colis_id
    assert data["livreur_id"] == livreur_id


def test_read_historique(client):
    # Créer une zone d'abord
    zone_data = {"nom": "Zone Est", "ville": "Fès", "code_postal": "30000"}
    zone_response = client.post("/zones", json=zone_data)
    assert zone_response.status_code == 201
    zone_name = zone_response.json()["nom"]

    # Créer un livreur
    livreur_data = {
        "nom": "Fatima",
        "prenom": "Test",
        "telephone": "0698765432",
        "vehicule": "VAN",
        "zone": zone_name
    }
    livreur_response = client.post("/livreurs/", json=livreur_data)
    assert livreur_response.status_code == 201
    livreur_id = livreur_response.json()["id"]

    # Créer un client
    client_data = {
        "nom": "Historique",
        "prenom": "Client",
        "email": "historique.client@example.com",
        "adresse": "456 Rue Test",
        "telephone": "0611223344",
        "ville": "Fès"
    }
    client_response = client.post("/clients/", json=client_data)
    assert client_response.status_code == 200
    client_id = client_response.json()["id"]

    # Créer un destinataire
    destinataire_data = {
        "nom": "Destinataire",
        "prenom": "Historique",
        "email": "dest.hist@example.com",
        "telephone": "0655443322",
        "adresse": "789 Rue Destinataire"
    }
    destinataire_response = client.post("/destinataires/", json=destinataire_data)
    assert destinataire_response.status_code == 200
    destinataire_id = destinataire_response.json()["id"]

    # Créer un colis
    colis_data = {
        "description": "Test Colis Historique",
        "poids": 1.5,
        "statut": "CRÉE",
        "ville_destination": "Fès",
        "client_id": client_id,
        "destinataire_id": destinataire_id
    }
    colis_response = client.post("/colis/", json=colis_data)
    assert colis_response.status_code == 200
    colis_id = colis_response.json()["id"]

    # Créer deux historiques
    historique_data_1 = {
        "nouveau_statut": "EN_STOCK",
        "livreur_id": livreur_id
    }
    response_1 = client.post(f"/colis/{colis_id}/historiques", json=historique_data_1)
    assert response_1.status_code == 201
    # Le premier historique créé doit avoir ancien_statut="CREE" (le statut initial du colis)
    assert response_1.json()["ancien_statut"] == "CREE"
    assert response_1.json()["nouveau_statut"] == "EN_STOCK"

    historique_data_2 = {
        "nouveau_statut": "EN_TRANSIT",
        "livreur_id": livreur_id
    }
    response_2 = client.post(f"/colis/{colis_id}/historiques", json=historique_data_2)
    assert response_2.status_code == 201
    # Le deuxième historique doit avoir ancien_statut="EN_STOCK" (le dernier nouveau_statut)
    assert response_2.json()["ancien_statut"] == "EN_STOCK"
    assert response_2.json()["nouveau_statut"] == "EN_TRANSIT"

    # Lire les historiques
    response = client.get(f"/colis/{colis_id}/historiques")
    assert response.status_code == 200
    data = response.json()
    # 3 historiques: 1 créé automatiquement lors de la création du colis, + 2 ajoutés manuellement
    assert len(data) == 3
    assert data[0]["nouveau_statut"] == "CREE"  # Créé automatiquement
    assert data[0]["ancien_statut"] is None  # Premier statut
    assert data[1]["ancien_statut"] == "CREE"  # Transition: CREE -> EN_STOCK
    assert data[1]["nouveau_statut"] == "EN_STOCK"
    assert data[2]["ancien_statut"] == "EN_STOCK"  # Transition: EN_STOCK -> EN_TRANSIT
    assert data[2]["nouveau_statut"] == "EN_TRANSIT"