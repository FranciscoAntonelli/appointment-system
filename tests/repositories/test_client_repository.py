from src.entities.client import Client

def test_get_by_id_returns_client(client_repo, client):

    result = client_repo.get_by_id(client.id)

    assert result is not None
    

def test_get_by_id_returns_none_when_client_not_exists(repo):

    result = repo.get_by_id(999999)

    assert result is None