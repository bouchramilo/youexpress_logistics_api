

def test_create_colis(client):
    # specific data for the colis
    colis_data = {
        "description": "Electronic Components",
        "poids": 2.5,
        "statut": "PENDING",
        "ville_destination": "Casablanca",
        "client_id": 1  # This must match an existing client in the test DB
    }
    colis_response = client.post()

