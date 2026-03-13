import pytest

from app.core.messages import ACCESO_RESPUESTA, ADMINISTRACION_PERSONAL_MENU, BUSQUEDAS_MENU, CERTIFICADO_RESPUESTA, FALLBACK_MAIN_MENU, FALLBACK_MODULE_MENU, LICENCIAS_DISPONIBLES_RESPUESTA, SERVICIO_MEDICO_MENU, SOPORTE_MENU, VOLVER_MENU_PRINCIPAL
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


@pytest.mark.parametrize(
    "initial_flow_state",
    [
        "administracion_personal_menu",
        "justificar_licencias_menu",
        "licencias_disponibles",
        "busquedas_internas_menu",
        "servicio_medico_menu",
        "soporte_menu",
    ],
)
def test_flow_engine_returns_to_main_menu_from_submenus(
    initial_flow_state: str,
) -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state=initial_flow_state,
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
        "volver",
        "menu",
        "menú",
        "inicio",
    ],
)
def test_flow_engine_returns_to_main_menu_from_administracion_personal_menu_aliases(
    user_input: str,
) -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="administracion_personal_menu",
    )

    result = engine.next_step(state=state, user_input=user_input)

    assert result.flow_state == "main_menu"
    assert result.reply_text == VOLVER_MENU_PRINCIPAL


def test_flow_engine_routes_to_licencias_disponibles_with_reply_text() -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="administracion_personal_menu",
    )

    result = engine.next_step(state=state, user_input="disponibles")

    assert result.flow_state == "licencias_disponibles"
    assert result.reply_text == LICENCIAS_DISPONIBLES_RESPUESTA


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


@pytest.mark.parametrize(
    "user_input",
    [
        "busquedas",
        "busqueda",
    ],
)
def test_flow_engine_routes_from_main_menu_to_busquedas_internas(
    user_input: str,
) -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="main_menu",
    )

    result = engine.next_step(state=state, user_input=user_input)

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


@pytest.mark.parametrize(
    "user_input",
    [
        "turno",
        "medico",
        "certificado",
    ],
)
def test_flow_engine_returns_servicio_medico_response(
    user_input: str,
) -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="servicio_medico_menu",
    )

    result = engine.next_step(state=state, user_input=user_input)

    assert result.flow_state == "servicio_medico_menu"
    assert result.reply_text == CERTIFICADO_RESPUESTA


def test_flow_engine_routes_from_main_menu_to_soporte() -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="main_menu",
    )

    result = engine.next_step(state=state, user_input="soporte")

    assert result.flow_state == "soporte_menu"
    assert result.reply_text == SOPORTE_MENU


@pytest.mark.parametrize(
    "user_input",
    [
        "soporte",
        "acceso",
        "problema",
        "app",
    ],
)
def test_flow_engine_returns_soporte_response(
    user_input: str,
) -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="soporte_menu",
    )

    result = engine.next_step(state=state, user_input=user_input)

    assert result.flow_state == "soporte_menu"
    assert result.reply_text == ACCESO_RESPUESTA


def test_flow_engine_returns_main_menu_fallback() -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="main_menu",
    )

    result = engine.next_step(state=state, user_input="asdf")

    assert result.flow_state == "main_menu"
    assert result.reply_text == FALLBACK_MAIN_MENU


@pytest.mark.parametrize(
    ("user_input", "expected_flow_state"),
    [
        ("a", "justificar_vacaciones"),
        ("examen", "justificar_examen"),
        ("mudanza", "justificar_mudanza"),
    ],
)
def test_flow_engine_routes_from_justificar_licencias_menu(
    user_input: str, expected_flow_state: str
) -> None:
    engine = FlowEngine()
    state = ConversationState(
        session_id="test-session",
        flow_state="justificar_licencias_menu",
    )

    result = engine.next_step(state=state, user_input=user_input)

    assert result.flow_state == expected_flow_state
