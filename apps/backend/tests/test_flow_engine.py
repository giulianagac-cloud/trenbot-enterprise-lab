import pytest

from app.core.messages import ADMINISTRACION_PERSONAL_MENU, BUSQUEDAS_MENU, FALLBACK_MODULE_MENU, SERVICIO_MEDICO_MENU, VOLVER_MENU_PRINCIPAL
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


def test_flow_engine_returns_to_main_menu_from_licencias_disponibles() -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="licencias_disponibles",
    )

    result = engine.next_step(state=state, user_input="volver")

    assert result.flow_state == "main_menu"
    assert result.reply_text == VOLVER_MENU_PRINCIPAL


def test_flow_engine_returns_module_fallback_from_administracion_personal_menu() -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="administracion_personal_menu",
    )

    result = engine.next_step(state=state, user_input="asdf")

    assert result.flow_state == "administracion_personal_menu"
    assert result.reply_text == FALLBACK_MODULE_MENU


@pytest.mark.parametrize(
    "user_input",
    [
        "administracion",
        "admin",
        "adm personal",
        "personal",
        "licencias",
    ],
)
def test_flow_engine_routes_from_main_menu_to_administracion_personal(
    user_input: str,
) -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="main_menu",
    )

    result = engine.next_step(state=state, user_input=user_input)

    assert result.flow_state == "administracion_personal_menu"
    assert result.reply_text == ADMINISTRACION_PERSONAL_MENU


def test_flow_engine_routes_from_main_menu_to_busquedas_internas() -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="main_menu",
    )

    result = engine.next_step(state=state, user_input="busquedas")

    assert result.flow_state == "busquedas_internas_menu"
    assert result.reply_text == BUSQUEDAS_MENU


def test_flow_engine_routes_from_main_menu_to_servicio_medico() -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="main_menu",
    )

    result = engine.next_step(state=state, user_input="medico")

    assert result.flow_state == "servicio_medico_menu"
    assert result.reply_text == SERVICIO_MEDICO_MENU
