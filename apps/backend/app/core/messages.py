LICENCIAS_MENU = "¿Qué licencia querés justificar? Podés elegir: A. Vacaciones, B. Examen, C. Mudanza."

FORMULARIO_VACACIONES_URL = "/static/forms/vacaciones.pdf"
FORMULARIO_EXAMEN_URL = "/static/forms/examen.pdf"
FORMULARIO_MUDANZA_URL = "/static/forms/mudanza.pdf"
FORMULARIO_DDJJ_DOMICILIO_URL = "/static/forms/ddjj_domicilio.pdf"

VACACIONES_RESPUESTA = (
    "Para justificar vacaciones, la solicitud debe realizarse con 25 días de anticipación. "
    f"Podés descargar el formulario correspondiente aquí: {FORMULARIO_VACACIONES_URL}"
)

BUSQUEDAS_MENU = "Ingresaste al módulo de Búsquedas Internas."

VACANTES_RESPUESTA = (
    "Podés consultar búsquedas internas vigentes o futuras oportunidades dentro de la empresa."
)

SERVICIO_MEDICO_MENU = "Ingresaste al módulo de Servicio Médico."

CERTIFICADO_RESPUESTA = (
    "Podés consultar turnos, certificados médicos o gestiones vinculadas al Servicio Médico."
)

SOPORTE_MENU = "Ingresaste al módulo de Soporte."

ACCESO_RESPUESTA = (
    "Podés informar problemas de acceso, uso de la app o consultas de soporte interno."
)

FALLBACK_MAIN_MENU = (
    "TrenBot Enterprise puede asistirte en los siguientes módulos: "
    "Administración de Personal, Búsquedas Internas, Servicio Médico y Soporte."
)

FALLBACK_MODULE_MENU = "Podés continuar dentro del módulo actual o volver al menú principal."

VOLVER_MENU_PRINCIPAL = "Volviste al menú principal."

ADMINISTRACION_PERSONAL_MENU = "Ingresaste a Administración de Personal. Podés elegir: Licencias disponibles o Justificar licencias."

LICENCIAS_DISPONIBLES_RESPUESTA = (
    "Puedo ayudarte a consultar las licencias disponibles. "
    "Más adelante este flujo se conectará con SAP para informarte, por ejemplo, "
    "cuántos días de vacaciones tenés disponibles."
)

EXAMEN_RESPUESTA = (
    "Para justificar licencia por examen, debés presentar el comprobante correspondiente. "
    f"Podés descargar el formulario aquí: {FORMULARIO_EXAMEN_URL}"
)

MUDANZA_RESPUESTA = (
    "Para solicitar la licencia por mudanza, debés presentar el formulario de mudanza antes de gozar la licencia. "
    f"Podés descargarlo aquí: {FORMULARIO_MUDANZA_URL}\n\n"
    "Al reincorporarte, debés presentar también la DDJJ de nuevo domicilio. "
    f"Podés descargarla aquí: {FORMULARIO_DDJJ_DOMICILIO_URL}"
)
