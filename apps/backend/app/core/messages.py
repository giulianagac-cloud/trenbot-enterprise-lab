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

SERVICIO_MEDICO_MENU = (
    "Ingresaste al módulo de Servicio Médico. ¿En qué podemos ayudarte?\n"
    "A. Aviso de enfermedad\n"
    "B. Justificar licencia médica\n"
    "C. Consultar próxima cita"
)

AVISO_ENFERMEDAD_RESPUESTA = (
    "Para avisar una enfermedad, debés comunicarte con tu responsable directo y con el área de RRHH "
    "antes de las 9:00 hs del día de ausencia."
)

JUSTIFICAR_LICENCIA_MEDICA_MENU = (
    "¿Qué licencia médica querés justificar?\n"
    "A. Certificado médico\n"
    "B. Exodoncia\n"
    "C. Donación de sangre"
)

FORMULARIO_EXODONCIA_URL = "/static/forms/exodoncia.pdf"
FORMULARIO_DONACION_SANGRE_URL = "/static/forms/donacion_sangre.pdf"

CERTIFICADO_MEDICO_RESPUESTA = (
    "Para justificar una licencia médica, debés presentar el certificado emitido por el médico tratante "
    "dentro de las 48 hs de reincorporarte."
)

LICENCIA_EXODONCIA_RESPUESTA = (
    "Para justificar licencia por exodoncia, debés presentar el certificado del odontólogo. "
    f"Podés descargar el formulario aquí: {FORMULARIO_EXODONCIA_URL}"
)

LICENCIA_DONACION_SANGRE_RESPUESTA = (
    "Para justificar licencia por donación de sangre, debés presentar el comprobante del banco de sangre. "
    f"Podés descargar el formulario aquí: {FORMULARIO_DONACION_SANGRE_URL}"
)

PROXIMA_CITA_RESPUESTA = (
    "Próximamente este flujo se conectará con la plataforma SIMEF para informarte "
    "si tenés una próxima cita médica programada."
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
