from dataclasses import dataclass

from app.domain.conversation import ConversationState


@dataclass
class FlowResult:
    flow_state: str
    reply_text: str


class FlowEngine:
    def next_step(self, state: ConversationState, user_input: str) -> FlowResult:
        normalized = user_input.lower()

        if any(keyword in normalized for keyword in ("vacation", "leave", "time off")):
            return FlowResult(
                flow_state="leave_guidance",
                reply_text=(
                    "I can guide you through the leave request flow. "
                    "To start, tell me whether this is vacation, medical leave, or another absence type."
                ),
            )

        if any(keyword in normalized for keyword in ("salary", "payroll", "receipt")):
            return FlowResult(
                flow_state="payroll_support",
                reply_text=(
                    "I can help with payroll-related guidance. "
                    "Tell me whether you need a payslip, payment date information, or a payroll issue review."
                ),
            )

        return FlowResult(
            flow_state=state.flow_state,
            reply_text=(
                "I am ready to assist with HR requests. "
                "You can ask about leave, payroll, certificates, or internal employee processes."
            ),
        )

