import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"DevSecOps Dashboard" in response.data


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_status_endpoint():
    client = app.test_client()

    response = client.get("/api/status")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "running"


def test_info_endpoint():
    client = app.test_client()

    response = client.get("/api/info")

    assert response.status_code == 200

    data = response.get_json()

    assert data["technology"] == "Python Flask"