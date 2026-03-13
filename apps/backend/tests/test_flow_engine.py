import pytest

from app.domain.conversation import ConversationState
from app.services.flow_engine import FlowEngine


@pytest.mark.parametrize(
    ("user_input", "expected_flow_state"),
    [
        ("disponibles", "licencias_disponibles"),
        ("justificar", "justificar_licencias_menu"),
    ],
)
def test_flow_engine_routes_from_administracion_personal_menu(
    user_input: str, expected_flow_state: str
) -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="administracion_personal_menu",
    )

    result = engine.next_step(state=state, user_input=user_input)

    assert result.flow_state == expected_flow_state
