from fastapi.testclient import TestClient

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
    assert "leave request flow" in payload["reply"]["content"]

