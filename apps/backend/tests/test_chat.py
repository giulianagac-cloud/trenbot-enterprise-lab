from fastapi.testclient import TestClient

from app.core.messages import ADMINISTRACION_PERSONAL_MENU, FALLBACK_MODULE_MENU, VACANTES_RESPUESTA, VOLVER_MENU_PRINCIPAL
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


def test_chat_routes_back_to_main_menu_with_volver() -> None:
    response = client.post(
        "/chat",
        json={"session_id": "api-volver-test", "message": "administracion"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "administracion_personal_menu"

    response = client.post(
        "/chat",
        json={"session_id": "api-volver-test", "message": "volver"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "main_menu"
    assert payload["reply"]["content"] == VOLVER_MENU_PRINCIPAL


def test_chat_routes_conversational_flow_to_busquedas_internas() -> None:
    response = client.post(
        "/chat",
        json={"session_id": "api-busquedas-test", "message": "busquedas"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "busquedas_internas_menu"

    response = client.post(
        "/chat",
        json={"session_id": "api-busquedas-test", "message": "vacantes"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "busquedas_internas_menu"
    assert payload["reply"]["content"] == VACANTES_RESPUESTA


def test_chat_returns_module_fallback_within_soporte() -> None:
    response = client.post(
        "/chat",
        json={"session_id": "api-soporte-fallback-test", "message": "soporte"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "soporte_menu"

    response = client.post(
        "/chat",
        json={"session_id": "api-soporte-fallback-test", "message": "asdf"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "soporte_menu"
    assert payload["reply"]["content"] == FALLBACK_MODULE_MENU


def test_chat_returns_module_fallback_within_servicio_medico() -> None:
    response = client.post(
        "/chat",
        json={"session_id": "api-medico-fallback-test", "message": "medico"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "servicio_medico_menu"

    response = client.post(
        "/chat",
        json={"session_id": "api-medico-fallback-test", "message": "asdf"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "servicio_medico_menu"
    assert payload["reply"]["content"] == FALLBACK_MODULE_MENU


def test_chat_returns_module_fallback_within_busquedas_internas() -> None:
    response = client.post(
        "/chat",
        json={"session_id": "api-busquedas-fallback-test", "message": "busquedas"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "busquedas_internas_menu"

    response = client.post(
        "/chat",
        json={"session_id": "api-busquedas-fallback-test", "message": "asdf"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "busquedas_internas_menu"
    assert payload["reply"]["content"] == FALLBACK_MODULE_MENU


def test_chat_returns_module_fallback_within_justificar_licencias() -> None:
    response = client.post(
        "/chat",
        json={"session_id": "api-justificar-fallback-test", "message": "administracion"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "administracion_personal_menu"

    response = client.post(
        "/chat",
        json={"session_id": "api-justificar-fallback-test", "message": "justificar"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "justificar_licencias_menu"

    response = client.post(
        "/chat",
        json={"session_id": "api-justificar-fallback-test", "message": "asdf"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["flow_state"] == "justificar_licencias_menu"
    assert payload["reply"]["content"] == FALLBACK_MODULE_MENU

