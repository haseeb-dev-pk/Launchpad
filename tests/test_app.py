import json

from app import app


def test_home_page_renders():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Launchpad" in response.data
    assert b"Recent deployments" in response.data


def test_health_endpoint_is_machine_readable():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert json.loads(response.data)["status"] == "ok"


def test_ready_endpoint_is_available_for_orchestration():
    response = app.test_client().get("/ready")
    assert response.status_code == 200
    assert response.json == {"status": "ready"}