from dataclasses import dataclass

from app.core.messages import ACCESO_RESPUESTA, ADMINISTRACION_PERSONAL_MENU, BUSQUEDAS_MENU, CERTIFICADO_RESPUESTA, EXAMEN_RESPUESTA, LICENCIAS_DISPONIBLES_RESPUESTA, LICENCIAS_MENU, MUDANZA_RESPUESTA, SERVICIO_MEDICO_MENU, SOPORTE_MENU, VACACIONES_RESPUESTA, VACANTES_RESPUESTA, VOLVER_MENU_PRINCIPAL
from app.domain.conversation import ConversationState


@dataclass
class FlowResult:
    flow_state: str
    reply_text: str


class FlowEngine:
    def _handle_main_menu(
        self, state: ConversationState, normalized: str
    ) -> FlowResult | None:
        # Menú principal
        if state.flow_state == "main_menu":
            if any(word in normalized for word in ("administracion", "personal", "licencias", "admin")):
                return FlowResult(
                    flow_state="administracion_personal_menu",
                    reply_text=ADMINISTRACION_PERSONAL_MENU,
                )

            if any(word in normalized for word in ("busquedas", "busqueda")):
                return FlowResult(
                    flow_state="busquedas_internas_menu",
                    reply_text=BUSQUEDAS_MENU,
                )

            if any(word in normalized for word in ("medico", "servicio medico")):
                return FlowResult(
                    flow_state="servicio_medico_menu",
                    reply_text=SERVICIO_MEDICO_MENU,
                )

            if "soporte" in normalized:
                return FlowResult(
                    flow_state="soporte_menu",
                    reply_text=SOPORTE_MENU,
                )

        return None

    def _handle_busquedas_internas(
        self, state: ConversationState, normalized: str
    ) -> FlowResult | None:
        # Búsquedas Internas
        if state.flow_state == "busquedas_internas_menu":
            if any(word in normalized for word in ("vacantes", "internas", "busquedas")):
                return FlowResult(
                    flow_state="busquedas_internas_menu",
                    reply_text=VACANTES_RESPUESTA,
                )

        return None

    def _handle_servicio_medico(
        self, state: ConversationState, normalized: str
    ) -> FlowResult | None:
        # Servicio Médico
        if state.flow_state == "servicio_medico_menu":
            if any(word in normalized for word in ("turno", "medico", "certificado")):
                return FlowResult(
                    flow_state="servicio_medico_menu",
                    reply_text=CERTIFICADO_RESPUESTA,
                )

        return None

    def _handle_soporte(
        self, state: ConversationState, normalized: str
    ) -> FlowResult | None:
        # Soporte
        if state.flow_state == "soporte_menu":
            if any(word in normalized for word in ("app", "problema", "acceso", "soporte")):
                return FlowResult(
                    flow_state="soporte_menu",
                    reply_text=ACCESO_RESPUESTA,
                )

        return None

    def _handle_administracion_personal(
        self, state: ConversationState, normalized: str
    ) -> FlowResult | None:
        # Submenú Administración de Personal
        if state.flow_state == "administracion_personal_menu":
            if any(word in normalized for word in ("licencias disponibles", "disponibles", "vacaciones", "dias", "saldo")):
                return FlowResult(
                    flow_state="licencias_disponibles",
                    reply_text=LICENCIAS_DISPONIBLES_RESPUESTA,
                )

            if any(word in normalized for word in ("justificar", "licencia", "justificar licencia")):
                return FlowResult(
                    flow_state="justificar_licencias_menu",
                    reply_text=LICENCIAS_MENU,
                )

        return None

    def _handle_justificar_licencias(
        self, state: ConversationState, normalized: str
    ) -> FlowResult | None:
        # Menú Justificar Licencias
        if state.flow_state == "justificar_licencias_menu":
            if normalized in ("a", "a.") or any(word in normalized for word in ("vacaciones", "vacacion")):
                return FlowResult(
                    flow_state="justificar_vacaciones",
                    reply_text=VACACIONES_RESPUESTA,
                )

            if normalized in ("b", "b.") or any(word in normalized for word in ("examen", "examenes")):
                return FlowResult(
                    flow_state="justificar_examen",
                    reply_text=EXAMEN_RESPUESTA,
                )

            if normalized in ("c", "c.") or any(word in normalized for word in ("mudanza",)):
                return FlowResult(
                    flow_state="justificar_mudanza",
                    reply_text=MUDANZA_RESPUESTA,
                )

        return None

    def next_step(self, state: ConversationState, user_input: str) -> FlowResult:
        normalized = user_input.lower().strip()
        if state.flow_state in (
            "licencias_menu",
            "administracion_personal_menu",
            "justificar_licencias_menu",
            "busquedas_internas_menu",
            "servicio_medico_menu",
            "soporte_menu",
        ) and normalized in ("volver", "menu", "menú", "inicio"):
            return FlowResult(
                flow_state="main_menu",
                reply_text=VOLVER_MENU_PRINCIPAL
            )

        # Menú principal
        result = self._handle_main_menu(state, normalized)
        if result:
            return result

        # Búsquedas Internas
        result = self._handle_busquedas_internas(state, normalized)
        if result:
            return result

        # Servicio Médico
        result = self._handle_servicio_medico(state, normalized)
        if result:
            return result

        # Soporte
        result = self._handle_soporte(state, normalized)
        if result:
            return result

        # Administración de Personal
        result = self._handle_administracion_personal(state, normalized)
        if result:
            return result

        # Menú Justificar Licencias
        result = self._handle_justificar_licencias(state, normalized)
        if result:
            return result

        # Flujos genéricos heredados del scaffold
        if any(keyword in normalized for keyword in ("vacation", "leave", "time off")):
            return FlowResult(
                flow_state="leave_guidance",
                reply_text=(
                    "Puedo ayudarte con el circuito de licencias. "
                    "Para empezar, indicame si se trata de vacaciones, licencia médica u otro tipo de ausencia."
                ),
            )

        if any(keyword in normalized for keyword in ("salary", "payroll", "receipt")):
            return FlowResult(
                flow_state="payroll_support",
                reply_text=(
                    "Puedo ayudarte con temas de liquidación y recibo de sueldo. "
                    "Indicame si necesitás tu recibo, fecha de pago o revisar una incidencia de liquidación."
                ),
            )

        # Fallback contextual final
        # Respuesta por defecto
        return FlowResult(
            flow_state=state.flow_state,
            reply_text=(
                "TrenBot Enterprise puede asistirte en los siguientes módulos: Administración de Personal, "
                "Búsquedas Internas, Servicio Médico y Soporte."
                if state.flow_state == "main_menu"
                else "Podés continuar dentro del módulo actual o volver al menú principal."
            ),
        )
