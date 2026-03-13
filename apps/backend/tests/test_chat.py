from fastapi.testclient import TestClient

from app.core.messages import ADMINISTRACION_PERSONAL_MENU
from app.main import app


client = TestClient(app)


def test_chat_returns_guided_leave_response() -> None:
    response = client.post(
        "/chat",
        json={"session_id": "session-1", "message": "I need vacation information"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["session_id"] == "session-1"
    assert payload["flow_state"] == "leave_guidance"
    assert "circuito de licencias" in payload["reply"]["content"]


def test_chat_routes_to_administracion_personal_menu() -> None:
    response = client.post(
        "/chat",
        json={"session_id": "api-test", "message": "administracion"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["session_id"] == "api-test"
    assert payload["flow_state"] == "administracion_personal_menu"
    assert payload["reply"]["content"] == ADMINISTRACION_PERSONAL_MENU


def test_chat_routes_conversational_flow_to_justificar_vacaciones() -> None:
    response = client.post(
        "/chat",
        json={"session_id": "api-flow-test", "message": "administracion"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "administracion_personal_menu"

    response = client.post(
        "/chat",
        json={"session_id": "api-flow-test", "message": "justificar"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "justificar_licencias_menu"

    response = client.post(
        "/chat",
        json={"session_id": "api-flow-test", "message": "vacaciones"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "justificar_vacaciones"

